"""
Test the API endpoints to ensure they work correctly.
"""

import os
import sys
import tempfile
import zipfile
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from app import create_app


@pytest.fixture
def app():
    """Create and configure a test app."""
    # Create a temporary directory for test uploads
    temp_dir = tempfile.mkdtemp()
    
    app = create_app('testing')
    app.config.update({
        'TESTING': True,
        'UPLOAD_FOLDER': temp_dir,
        'MAX_UPLOAD_SIZE': 10,  # 10MB for testing
        'MAX_EXTRACTED_SIZE': 50,  # 50MB for testing
    })
    
    yield app
    
    # Cleanup
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


@pytest.fixture
def sample_zip():
    """Create a sample ZIP file for testing."""
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, 'test_dump.zip')
    
    # Create a simple ZIP file with some log content
    with zipfile.ZipFile(zip_path, 'w') as zf:
        # Add some sample log files
        zf.writestr('logs/rocket.chat.log', 
                   '2025-08-03T10:00:00.000Z info: Server started\n'
                   '2025-08-03T10:01:00.000Z error: Database connection failed\n')
        zf.writestr('support-dump-info.json', 
                   '{"version": "6.0.0", "timestamp": "2025-08-03T10:00:00.000Z"}')
    
    yield zip_path
    
    # Cleanup
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/api/health')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'version' in data


def test_upload_no_file(client):
    """Test upload endpoint with no file."""
    response = client.post('/api/upload')
    assert response.status_code == 400
    
    data = response.get_json()
    assert 'error' in data


def test_upload_empty_filename(client):
    """Test upload endpoint with empty filename."""
    response = client.post('/api/upload', data={'support_dump': (None, '')})
    assert response.status_code == 400
    
    data = response.get_json()
    assert 'error' in data


def test_upload_wrong_file_type(client):
    """Test upload endpoint with wrong file type."""
    response = client.post('/api/upload', data={
        'support_dump': (tempfile.NamedTemporaryFile(suffix='.txt'), 'test.txt')
    })
    assert response.status_code == 400
    
    data = response.get_json()
    assert 'File type not allowed' in data['error']


def test_upload_valid_file(client, sample_zip):
    """Test upload endpoint with valid ZIP file."""
    with open(sample_zip, 'rb') as f:
        response = client.post('/api/upload', data={
            'support_dump': (f, 'test_dump.zip')
        })
    
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'session_id' in data
    assert data['filename'] == 'test_dump.zip'


def test_analyze_invalid_session(client):
    """Test analyze endpoint with invalid session."""
    response = client.post('/api/analyze/invalid-session-id')
    assert response.status_code == 404
    
    data = response.get_json()
    assert 'Session not found' in data['error']


def test_get_results_invalid_session(client):
    """Test results endpoint with invalid session."""
    response = client.get('/api/results/invalid-session-id')
    assert response.status_code == 404
    
    data = response.get_json()
    assert 'Session not found' in data['error']


def test_list_sessions_empty(client):
    """Test sessions list when no sessions exist."""
    response = client.get('/api/sessions')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['active_sessions'] == 0
    assert data['sessions'] == {}


if __name__ == '__main__':
    # Run a simple test
    app = create_app('development')
    with app.test_client() as client:
        # Test health check
        response = client.get('/api/health')
        print(f"Health check: {response.status_code} - {response.get_json()}")
        
        # Test sessions list
        response = client.get('/api/sessions')
        print(f"Sessions list: {response.status_code} - {response.get_json()}")
        
    print("Basic API tests completed!")
