"""
Unit tests for the configuration module.
"""
import pytest
import os
from pathlib import Path
from config import Config, DevelopmentConfig, ProductionConfig, TestingConfig, get_config


class TestConfig:
    """Test cases for the Config class."""
    
    def test_default_values(self):
        """Test that default configuration values are set correctly."""
        config = Config()
        assert config.APP_NAME == "SAVA E-Commerce Platform"
        assert config.APP_VERSION == "1.0.0"
        assert config.DEFAULT_TAX_RATE == 0.08
        assert config.DEFAULT_SHIPPING_COST == 5.99
        assert config.PRODUCTS_PER_PAGE == 24
    
    def test_environment_variable_override(self, monkeypatch):
        """Test that environment variables override default values."""
        monkeypatch.setenv("DEFAULT_TAX_RATE", "0.10")
        monkeypatch.setenv("PRODUCTS_PER_PAGE", "12")
        
        # Reload config
        from importlib import reload
        import config as config_module
        reload(config_module)
        
        assert config_module.Config.DEFAULT_TAX_RATE == 0.10
        assert config_module.Config.PRODUCTS_PER_PAGE == 12
    
    def test_secret_key_generation(self):
        """Test that SECRET_KEY is generated if not provided."""
        config = Config()
        assert config.SECRET_KEY is not None
        assert len(config.SECRET_KEY) >= 32


class TestDevelopmentConfig:
    """Test cases for DevelopmentConfig."""
    
    def test_development_settings(self):
        """Test development-specific settings."""
        config = DevelopmentConfig()
        assert config.DEBUG is True
        assert config.ENVIRONMENT == 'development'
        assert config.LOG_LEVEL == 'DEBUG'


class TestProductionConfig:
    """Test cases for ProductionConfig."""
    
    def test_production_settings(self):
        """Test production-specific settings."""
        config = ProductionConfig()
        assert config.DEBUG is False
        assert config.ENVIRONMENT == 'production'
        assert config.LOG_LEVEL == 'WARNING'
        assert config.RATE_LIMIT_ENABLED is True


class TestTestingConfig:
    """Test cases for TestingConfig."""
    
    def test_testing_settings(self):
        """Test testing-specific settings."""
        config = TestingConfig()
        assert config.DEBUG is True
        assert config.ENVIRONMENT == 'testing'
        assert config.LOG_LEVEL == 'DEBUG'


class TestGetConfig:
    """Test cases for get_config function."""
    
    def test_get_development_config(self):
        """Test getting development configuration."""
        config = get_config('development')
        assert config == DevelopmentConfig
    
    def test_get_production_config(self, monkeypatch):
        """Test getting production configuration."""
        # Set required environment variables for production
        monkeypatch.setenv("SECRET_KEY", "a" * 64)
        monkeypatch.setenv("FIREBASE_DATABASE_URL", "https://test.firebaseio.com")
        
        config = get_config('production')
        assert config == ProductionConfig
    
    def test_get_testing_config(self):
        """Test getting testing configuration."""
        config = get_config('testing')
        assert config == TestingConfig
    
    def test_default_to_development(self):
        """Test that configuration defaults to development."""
        config = get_config()
        assert config == DevelopmentConfig


class TestConfigValidation:
    """Test cases for configuration validation."""
    
    def test_production_validation_with_missing_secret(self, monkeypatch):
        """Test that production validation fails with missing SECRET_KEY."""
        monkeypatch.setenv("ENVIRONMENT", "production")
        monkeypatch.delenv("SECRET_KEY", raising=False)
        
        with pytest.raises(ValueError, match="SECRET_KEY"):
            get_config('production')
    
    def test_production_validation_with_short_secret(self, monkeypatch):
        """Test that production validation fails with short SECRET_KEY."""
        monkeypatch.setenv("ENVIRONMENT", "production")
        monkeypatch.setenv("SECRET_KEY", "short")
        
        with pytest.raises(ValueError, match="SECRET_KEY"):
            get_config('production')
    
    def test_get_env_info(self):
        """Test get_env_info method."""
        info = Config.get_env_info()
        assert 'app_name' in info
        assert 'version' in info
        assert 'environment' in info
        assert 'debug' in info
        assert 'log_level' in info
        
        # Should not include sensitive information
        assert 'SECRET_KEY' not in info
        assert 'PAYMENT_SECRET' not in info
