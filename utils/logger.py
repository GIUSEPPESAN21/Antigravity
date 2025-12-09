"""
Centralized logging configuration for the e-commerce platform.
Provides structured logging with file rotation and different log levels.
"""
import logging
import logging.handlers
from pathlib import Path
from typing import Optional
import sys

from config import active_config


class Logger:
    """Centralized logger with file and console handlers."""
    
    _loggers = {}
    _initialized = False
    
    @classmethod
    def _setup_logging(cls):
        """Set up logging configuration (only once)."""
        if cls._initialized:
            return
        
        # Create logs directory if it doesn't exist
        log_dir = Path(active_config.LOG_FILE).parent
        log_dir.mkdir(parents=True, exist_ok=True)
        
       # Get log level from config
        log_level = getattr(logging, active_config.LOG_LEVEL.upper(), logging.INFO)
        
        cls._initialized = True
    
    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Get or create a logger with the specified name.
        
        Args:
            name: Logger name (typically __name__ from the calling module)
            
        Returns:
            Configured logger instance
        """
        if name in cls._loggers:
            return cls._loggers[name]
        
        cls._setup_logging()
        
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, active_config.LOG_LEVEL.upper(), logging.INFO))
        
        # Prevent duplicate handlers
        if logger.handlers:
            return logger
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG if active_config.DEBUG else logging.INFO)
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        
        # File handler with rotation (10MB max, keep 5 backup files)
        try:
            file_handler = logging.handlers.RotatingFileHandler(
                active_config.LOG_FILE,
                maxBytes=10 * 1024 * 1024,  # 10MB
                backupCount=5,
                encoding='utf-8'
            )
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
        except Exception as e:
            logger.error(f"Failed to create file handler: {e}")
        
        cls._loggers[name] = logger
        return logger
    
    @classmethod
    def log_exception(cls, logger: logging.Logger, exc: Exception, context: Optional[str] = None):
        """
        Log an exception with full traceback.
        
        Args:
            logger: Logger instance
            exc: Exception to log
            context: Optional context string
        """
        if context:
            logger.exception(f"{context}: {str(exc)}")
        else:
            logger.exception(f"Exception occurred: {str(exc)}")


# Convenience function for quick logger access
def get_logger(name: str) -> logging.Logger:
    """Get a logger instance. Shorthand for Logger.get_logger()."""
    return Logger.get_logger(name)


# Example usage:
# from utils.logger import get_logger
# logger = get_logger(__name__)
# logger.info("Application started")
