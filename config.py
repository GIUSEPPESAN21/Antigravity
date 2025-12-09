"""
Configuration module for the Streamlit e-commerce platform.
Loads environment variables and provides configuration for different environments.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Determine the base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from .env file
env_path = BASE_DIR / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)


class Config:
    """Base configuration class with common settings."""
    
    # App settings
    APP_NAME = "SAVA E-Commerce Platform"
    APP_VERSION = "1.0.0"
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Environment
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32).hex()
    
    # Firebase Configuration
    FIREBASE_SERVICE_ACCOUNT_PATH = os.environ.get(
        'FIREBASE_SERVICE_ACCOUNT_PATH',
        str(BASE_DIR / 'firebase-service-account.json')
    )
    FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL', '')
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = os.environ.get('LOG_FILE', str(BASE_DIR / 'logs' / 'app.log'))
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Upload Configuration
    MAX_FILE_SIZE_MB = int(os.environ.get('MAX_FILE_SIZE_MB', 10))
    ALLOWED_IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', str(BASE_DIR / 'static' / 'uploads'))
    
    # Email Configuration (optional)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_FROM = os.environ.get('MAIL_FROM', MAIL_USERNAME)
    
    # Payment Configuration (placeholder)
    PAYMENT_API_KEY = os.environ.get('PAYMENT_API_KEY')
    PAYMENT_SECRET = os.environ.get('PAYMENT_SECRET')
    PAYMENT_MODE = os.environ.get('PAYMENT_MODE', 'sandbox')  # sandbox or production
    
    # Cart and Order Settings
    CART_SESSION_TIMEOUT = int(os.environ.get('CART_SESSION_TIMEOUT', 3600))  # 1 hour
    DEFAULT_TAX_RATE = float(os.environ.get('DEFAULT_TAX_RATE', 0.08))  # 8%
    DEFAULT_SHIPPING_COST = float(os.environ.get('DEFAULT_SHIPPING_COST', 5.99))
    FREE_SHIPPING_THRESHOLD = float(os.environ.get('FREE_SHIPPING_THRESHOLD', 50.00))
    
    # Pagination
    PRODUCTS_PER_PAGE = int(os.environ.get('PRODUCTS_PER_PAGE', 24))
    ORDERS_PER_PAGE = int(os.environ.get('ORDERS_PER_PAGE', 10))
    
    # Cache settings
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
    CACHE_DEFAULT_TIMEOUT = int(os.environ.get('CACHE_DEFAULT_TIMEOUT', 300))
    
    # Rate Limiting
    RATE_LIMIT_ENABLED = os.environ.get('RATE_LIMIT_ENABLED', 'False').lower() == 'true'
    RATE_LIMIT_PER_MINUTE = int(os.environ.get('RATE_LIMIT_PER_MINUTE', 60))
    
    @classmethod
    def validate(cls):
        """Validate critical configuration settings."""
        errors = []
        
        if cls.ENVIRONMENT == 'production':
            if not cls.SECRET_KEY or len(cls.SECRET_KEY) < 32:
                errors.append("SECRET_KEY must be set and at least 32 characters in production")
            
            if not cls.FIREBASE_SERVICE_ACCOUNT_PATH or not Path(cls.FIREBASE_SERVICE_ACCOUNT_PATH).exists():
                errors.append("FIREBASE_SERVICE_ACCOUNT_PATH must exist in production")
            
            if not cls.FIREBASE_DATABASE_URL:
                errors.append("FIREBASE_DATABASE_URL must be set in production")
        
        return errors
    
    @classmethod
    def get_env_info(cls):
        """Get environment information (for debugging, excludes sensitive data)."""
        return {
            'app_name': cls.APP_NAME,
            'version': cls.APP_VERSION,
            'environment': cls.ENVIRONMENT,
            'debug': cls.DEBUG,
            'log_level': cls.LOG_LEVEL,
        }


class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    ENVIRONMENT = 'development'
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False
    ENVIRONMENT = 'production'
    LOG_LEVEL = 'WARNING'
    RATE_LIMIT_ENABLED = True


class TestingConfig(Config):
    """Testing environment configuration."""
    DEBUG = True
    ENVIRONMENT = 'testing'
    LOG_LEVEL = 'DEBUG'


# Configuration dictionary
_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}


def get_config(env=None):
    """
    Get configuration object based on environment.
    
    Args:
        env: Environment name (development, production, testing)
        
    Returns:
        Configuration class for the specified environment
    """
    if env is None:
        env = os.environ.get('ENVIRONMENT', 'development')
    
    config_class = _config.get(env.lower(), DevelopmentConfig)
    
    # Validate configuration in production
    if env == 'production':
        errors = config_class.validate()
        if errors:
            raise ValueError(f"Configuration errors: {', '.join(errors)}")
    
    return config_class


# Export the active configuration
active_config = get_config()

