"""
API routes for the Rocket.Chat Log Analyzer.

This module provides REST API endpoints for:
- File upload and validation
- Log analysis triggers
- Results retrieval
- Export functionality
"""

from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
import uuid
import tempfile
from typing import Dict, Any, Optional
from pathlib import Path

# Import existing analysis logic
import analyzer
from utils import validate_zip_file, safe_extract_zip, ValidationError, LOG_LEVEL_NAMES


# Create API blueprint
api = Blueprint('api', __name__)

# In-memory session storage (will be replaced with database in future)
analysis_sessions: Dict[str, Dict[str, Any]] = {}


@api.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'rocketchat-log-analyzer-api',
        'version': '2.2.0-dev'
    })


@api.route('/upload', methods=['POST'])
def upload_file():
    """
    Upload and validate a support dump file.
    
    Returns:
        JSON response with session_id for tracking the analysis
    """
    if 'support_dump' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400
        
    file = request.files['support_dump']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
        
    if not file or not _allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed. Please upload a ZIP file.'}), 400
    
    try:
        # Create unique session
        session_id = str(uuid.uuid4())
        filename = secure_filename(file.filename)
        
        # Create session directory
        upload_folder = str(current_app.config['UPLOAD_FOLDER'])
        session_dir = os.path.join(upload_folder, session_id)
        os.makedirs(session_dir, exist_ok=True)
        
        # Save uploaded file
        file_path = os.path.join(session_dir, filename)
        file.save(file_path)
        
        # Validate the uploaded ZIP file
        from pathlib import Path
        validate_zip_file(
            Path(file_path), 
            current_app.config['MAX_CONTENT_LENGTH'], 
            current_app.config['MAX_EXTRACTED_SIZE']
        )
        
        # Store session info
        analysis_sessions[session_id] = {
            'file_path': file_path,
            'filename': filename,
            'status': 'uploaded',
            'results': None,
            'created_at': None,  # Will be set during analysis
            'error': None
        }
        
        return jsonify({
            'session_id': session_id,
            'status': 'success',
            'message': 'File uploaded and validated successfully',
            'filename': filename
        }), 200
        
    except ValidationError as e:
        # Clean up on validation error
        if 'session_id' in locals():
            _cleanup_session(session_id)
        return jsonify({'error': str(e)}), 400
        
    except Exception as e:
        # Clean up on unexpected error
        if 'session_id' in locals():
            _cleanup_session(session_id)
        current_app.logger.error(f"Upload error: {str(e)}")
        return jsonify({'error': 'Internal server error during upload'}), 500


@api.route('/analyze/<session_id>', methods=['POST'])
def analyze_logs(session_id: str):
    """
    Trigger analysis for an uploaded file.
    
    Args:
        session_id: The session identifier from upload
        
    Expected JSON body:
        {
            "log_level": "info"  # Optional: debug, info, warn, error
        }
    """
    if session_id not in analysis_sessions:
        return jsonify({'error': 'Session not found'}), 404
    
    session = analysis_sessions[session_id]
    if session['status'] != 'uploaded':
        return jsonify({'error': 'File not ready for analysis'}), 400
    
    try:
        # Get analysis parameters
        data = request.get_json() or {}
        log_level = data.get('log_level', 'info')
        
        if log_level not in LOG_LEVEL_NAMES.values():
            return jsonify({
                'error': f'Invalid log level. Must be one of: {", ".join(LOG_LEVEL_NAMES.values())}'
            }), 400
        
        # Extract the ZIP file
        from pathlib import Path
        extract_dir = os.path.join(os.path.dirname(session['file_path']), 'extracted')
        dump_path = safe_extract_zip(
            session['file_path'], 
            Path(extract_dir), 
            current_app.config['MAX_SINGLE_FILE_SIZE']
        )
        
        # Run analysis using existing analyzer
        current_app.logger.info(f"Starting analysis for session {session_id}")
        session['status'] = 'analyzing'
        
        # Call existing analysis function
        results = analyzer.analyze_logs(dump_path, log_level)
        
        # Update session with results
        session['status'] = 'completed'
        session['results'] = results
        session['created_at'] = results.get('analysis_info', {}).get('timestamp')
        
        # Return summary (not full results to avoid large response)
        summary = results.get('summary', {})
        
        return jsonify({
            'status': 'success',
            'message': 'Analysis completed successfully',
            'session_id': session_id,
            'summary': summary
        }), 200
        
    except Exception as e:
        session['status'] = 'error'
        session['error'] = str(e)
        current_app.logger.error(f"Analysis error for session {session_id}: {str(e)}")
        return jsonify({'error': 'Analysis failed', 'details': str(e)}), 500


@api.route('/results/<session_id>', methods=['GET'])
def get_results(session_id: str):
    """
    Retrieve analysis results for a session.
    
    Args:
        session_id: The session identifier
    """
    if session_id not in analysis_sessions:
        return jsonify({'error': 'Session not found'}), 404
    
    session = analysis_sessions[session_id]
    
    if session['status'] == 'error':
        return jsonify({
            'error': 'Analysis failed', 
            'details': session.get('error', 'Unknown error')
        }), 500
    
    if session['status'] != 'completed':
        return jsonify({
            'error': 'Analysis not complete', 
            'status': session['status']
        }), 400
    
    return jsonify(session['results']), 200


@api.route('/sessions/<session_id>', methods=['DELETE'])
def cleanup_session(session_id: str):
    """
    Clean up a session and its associated files.
    
    Args:
        session_id: The session identifier
    """
    if session_id not in analysis_sessions:
        return jsonify({'error': 'Session not found'}), 404
    
    try:
        _cleanup_session(session_id)
        return jsonify({'message': 'Session cleaned up successfully'}), 200
    except Exception as e:
        current_app.logger.error(f"Cleanup error for session {session_id}: {str(e)}")
        return jsonify({'error': 'Failed to cleanup session'}), 500


@api.route('/sessions', methods=['GET'])
def list_sessions():
    """
    List all active sessions (for debugging/admin purposes).
    """
    sessions_info = {}
    for sid, session in analysis_sessions.items():
        sessions_info[sid] = {
            'status': session['status'],
            'filename': session.get('filename'),
            'created_at': session.get('created_at'),
            'has_error': session.get('error') is not None
        }
    
    return jsonify({
        'active_sessions': len(sessions_info),
        'sessions': sessions_info
    }), 200


def _allowed_file(filename: str) -> bool:
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'zip'}


def _cleanup_session(session_id: str) -> None:
    """Clean up session files and remove from memory."""
    if session_id in analysis_sessions:
        session = analysis_sessions[session_id]
        
        # Remove session directory and all files
        session_dir = os.path.dirname(session['file_path'])
        if os.path.exists(session_dir):
            import shutil
            shutil.rmtree(session_dir, ignore_errors=True)
        
        # Remove from memory
        del analysis_sessions[session_id]


@api.errorhandler(404)
def not_found(error):
    """Handle 404 errors for API routes."""
    return jsonify({'error': 'Endpoint not found'}), 404


@api.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors for API routes."""
    return jsonify({'error': 'Method not allowed'}), 405


@api.errorhandler(500)
def internal_error(error):
    """Handle 500 errors for API routes."""
    return jsonify({'error': 'Internal server error'}), 500
