# utils.py
import zipfile
import tempfile
import logging
from pathlib import Path
from typing import Optional, Tuple
from werkzeug.utils import secure_filename

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_zip_file(file_path: Path, max_size: int, max_extracted_size: int) -> None:
    """
    Validate a ZIP file for security and size constraints.
    
    Args:
        file_path: Path to the ZIP file
        max_size: Maximum allowed ZIP file size in bytes
        max_extracted_size: Maximum allowed total extracted size in bytes
        
    Raises:
        ValidationError: If validation fails
    """
    # Check file size
    if file_path.stat().st_size > max_size:
        raise ValidationError(f"File too large: {file_path.stat().st_size} bytes (max: {max_size})")
    
    # Check ZIP structure and extracted size
    total_extracted_size = 0
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Check for zip bomb by examining compression ratios
            for info in zip_ref.infolist():
                # Skip directories
                if info.is_dir():
                    continue
                    
                # Check for suspicious compression ratios (potential zip bomb)
                if info.compress_size > 0:
                    ratio = info.file_size / info.compress_size
                    if ratio > 100:  # Compression ratio threshold
                        raise ValidationError(
                            f"Suspicious compression ratio for {info.filename}: {ratio:.1f}:1"
                        )
                
                total_extracted_size += info.file_size
                
                # Check total extracted size
                if total_extracted_size > max_extracted_size:
                    raise ValidationError(
                        f"Total extracted size too large: {total_extracted_size} bytes (max: {max_extracted_size})"
                    )
                    
    except zipfile.BadZipFile:
        raise ValidationError("Invalid ZIP file format")
    except Exception as e:
        if isinstance(e, ValidationError):
            raise
        raise ValidationError(f"Error validating ZIP file: {str(e)}")

def safe_extract_zip(file_path: Path, extract_path: Path, max_single_file_size: int) -> None:
    """
    Safely extract a ZIP file with security checks.
    
    Args:
        file_path: Path to the ZIP file
        extract_path: Directory to extract files to
        max_single_file_size: Maximum size for any single extracted file
        
    Raises:
        ValidationError: If extraction fails security checks
    """
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            for member in zip_ref.infolist():
                # Skip directories
                if member.is_dir():
                    continue
                    
                # Validate filename to prevent directory traversal
                if '..' in member.filename or member.filename.startswith('/'):
                    logging.warning(f"Skipping potentially malicious path: {member.filename}")
                    continue
                
                # Check individual file size
                if member.file_size > max_single_file_size:
                    logging.warning(f"Skipping large file: {member.filename} ({member.file_size} bytes)")
                    continue
                
                # Extract the file
                zip_ref.extract(member, extract_path)
                
    except zipfile.BadZipFile:
        raise ValidationError("Invalid ZIP file format during extraction")
    except Exception as e:
        raise ValidationError(f"Error extracting ZIP file: {str(e)}")

def find_dump_path(base_path: Path) -> Optional[Path]:
    """
    Robustly finds the correct directory containing the support dump files.
    
    Args:
        base_path: Base directory to search in
        
    Returns:
        Path to the dump directory, or None if not found
    """
    # Look for server-statistics.json as primary indicator
    for path in base_path.rglob('*server-statistics.json'):
        return path.parent
    
    # Fallback: look for any log.json files
    if any(base_path.glob('*log.json')):
        return base_path
        
    return None

def get_safe_filename(filename: str) -> str:
    """
    Get a safe filename using werkzeug's secure_filename.
    
    Args:
        filename: Original filename
        
    Returns:
        Secure filename
    """
    return secure_filename(filename)

def setup_logging(level: int = logging.INFO) -> None:
    """
    Set up application logging.
    
    Args:
        level: Logging level
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# Log level names mapping for reports
LOG_LEVEL_NAMES = {
    10: 'DEBUG', 
    20: 'INFO', 
    30: 'WARNING', 
    40: 'ERROR', 
    50: 'CRITICAL'
}
