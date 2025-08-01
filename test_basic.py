# test_basic.py
"""Basic tests for the RocketChat Log Analyzer."""

import pytest
import tempfile
import zipfile
from pathlib import Path
from app import create_app
from utils import validate_zip_file, ValidationError, get_safe_filename

class TestConfiguration:
    """Test configuration management."""
    
    def test_create_app_development(self):
        """Test app creation with development config."""
        app = create_app('development')
        assert app.config['DEBUG'] is True
        assert 'SECRET_KEY' in app.config
        
    def test_create_app_testing(self):
        """Test app creation with testing config."""
        app = create_app('testing')
        assert app.config['TESTING'] is True
        assert app.config['SECRET_KEY'] == 'testing-key'

class TestSecurity:
    """Test security features."""
    
    def test_safe_filename(self):
        """Test filename sanitization."""
        assert get_safe_filename("../../../etc/passwd") == "etc_passwd"
        assert get_safe_filename("normal_file.zip") == "normal_file.zip"
        assert get_safe_filename("file with spaces.zip") == "file_with_spaces.zip"
    
    def test_zip_validation_size_limit(self):
        """Test ZIP file size validation."""
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp:
            tmp_path = Path(tmp.name)
            
        # Create a small ZIP file
        with zipfile.ZipFile(tmp_path, 'w') as zf:
            zf.writestr("test.txt", "Hello World")
        
        # Should pass with generous limits
        validate_zip_file(tmp_path, 1024*1024, 1024*1024)  # 1MB limits
        
        # Should fail with very small limits
        with pytest.raises(ValidationError, match="File too large"):
            validate_zip_file(tmp_path, 10, 1024*1024)  # 10 byte limit
        
        tmp_path.unlink()
    
    def test_zip_validation_compression_ratio(self):
        """Test ZIP bomb detection via compression ratio."""
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp:
            tmp_path = Path(tmp.name)
            
        # Create a highly compressed file (potential zip bomb)
        with zipfile.ZipFile(tmp_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            # Create a file with lots of repeated data (compresses well)
            large_content = "A" * 10000  # 10KB of repeated 'A's
            zf.writestr("bomb.txt", large_content)
        
        # This should FAIL validation due to high compression ratio
        with pytest.raises(ValidationError, match="Suspicious compression ratio"):
            validate_zip_file(tmp_path, 1024*1024, 1024*1024)
        
        tmp_path.unlink()

class TestApp:
    """Test Flask application."""
    
    def test_index_get(self):
        """Test GET request to index."""
        app = create_app('testing')
        # Need to configure Flask properly for testing
        app.config['TESTING'] = True
        with app.test_client() as client:
            with app.app_context():
                response = client.get('/')
                assert response.status_code == 200
    
    def test_index_post_no_file(self):
        """Test POST request without file."""
        app = create_app('testing')
        app.config['TESTING'] = True
        with app.test_client() as client:
            with app.app_context():
                response = client.post('/')
                assert response.status_code == 200
                # Should redirect back to upload page with error

if __name__ == '__main__':
    pytest.main([__file__])
