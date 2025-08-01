# config.py
import os
from pathlib import Path

class Config:
    """Application configuration class."""
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    
    # File Upload Settings
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_UPLOAD_SIZE', 100 * 1024 * 1024))  # 100 MB default
    MAX_EXTRACTED_SIZE = int(os.environ.get('MAX_EXTRACTED_SIZE', 500 * 1024 * 1024))  # 500 MB default
    MAX_SINGLE_FILE_SIZE = int(os.environ.get('MAX_SINGLE_FILE_SIZE', 50 * 1024 * 1024))  # 50 MB default
    
    # Application Settings
    VERSION = "2.1.2"
    UPLOAD_FOLDER = Path(os.environ.get('UPLOAD_FOLDER', 'temp'))
    REPORTS_FOLDER = Path(os.environ.get('REPORTS_FOLDER', 'reports'))
    
    # Flask Settings
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')
    TESTING = os.environ.get('FLASK_TESTING', 'False').lower() in ('true', '1', 'yes')
    
    # Allowed file extensions
    ALLOWED_EXTENSIONS = {'zip'}
    
    @staticmethod
    def init_app(app):
        """Initialize application with this config."""
        pass

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    
    @staticmethod
    def init_app(app):
        Config.init_app(app)
        
        # Log to stderr in production
        import logging
        from logging import StreamHandler
        
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SECRET_KEY = 'testing-key'
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB for testing

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
