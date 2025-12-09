"""
Centralized error handling and custom exceptions for the e-commerce platform.
"""
from typing import Optional, Dict, Any
import streamlit as st
from utils.logger import get_logger

logger = get_logger(__name__)


# Custom Exceptions
class EcommerceException(Exception):
    """Base exception for all e-commerce related errors."""
    
    def __init__(self, message: str, error_code: Optional[str] = None, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.error_code = error_code or "GENERAL_ERROR"
        self.details = details or {}
        super().__init__(self.message)


class AuthenticationError(EcommerceException):
    """Raised when authentication fails."""
    
    def __init__(self, message: str = "Authentication failed", **kwargs):
        super().__init(message, error_code="AUTH_ERROR", **kwargs)


class ValidationError(EcommerceException):
    """Raised when input validation fails."""
    
    def __init__(self, message: str, field: Optional[str] = None, **kwargs):
        details = kwargs.get('details', {})
        if field:
            details['field'] = field
        kwargs['details'] = details
        super().__init__(message, error_code="VALIDATION_ERROR", **kwargs)


class DatabaseError(EcommerceException):
    """Raised when database operations fail."""
    
    def __init__(self, message: str = "Database operation failed", **kwargs):
        super().__init__(message, error_code="DB_ERROR", **kwargs)


class PaymentError(EcommerceException):
    """Raised when payment processing fails."""
    
    def __init__(self, message: str = "Payment processing failed", **kwargs):
        super().__init__(message, error_code="PAYMENT_ERROR", **kwargs)


class ProductNotFoundError(EcommerceException):
    """Raised when a product is not found."""
    
    def __init__(self, product_id: str, **kwargs):
        message = f"Product with ID '{product_id}' not found"
        super().__init__(message, error_code="PRODUCT_NOT_FOUND", details={'product_id': product_id}, **kwargs)


class InsufficientStockError(EcommerceException):
    """Raised when there is insufficient stock for a product."""
    
    def __init__(self, product_id: str, requested: int, available: int, **kwargs):
        message = f"Insufficient stock for product '{product_id}': requested {requested}, available {available}"
        super().__init__(
            message,
            error_code="INSUFFICIENT_STOCK",
            details={'product_id': product_id, 'requested': requested, 'available': available},
            **kwargs
        )


class CartError(EcommerceException):
    """Raised when cart operations fail."""
    
    def __init__(self, message: str = "Cart operation failed", **kwargs):
        super().__init__(message, error_code="CART_ERROR", **kwargs)


class ConfigurationError(EcommerceException):
    """Raised when configuration is invalid or missing."""
    
    def __init__(self, message: str = "Configuration error", **kwargs):
        super().__init__(message, error_code="CONFIG_ERROR", **kwargs)


# Error Handler
class ErrorHandler:
    """Centralized error handling for the application."""
    
    @staticmethod
    def handle_error(
        error: Exception,
        user_message: Optional[str] = None,
        show_details_in_debug: bool = True,
        log_level: str = "error"
    ):
        """
        Handle an error by logging it and displaying an appropriate message to the user.
        
        Args:
            error: The exception that occurred
            user_message: Optional user-friendly message (auto-generated if not provided)
            show_details_in_debug: Whether to show error details in debug mode
            log_level: Logging level (error, warning, info)
        """
        from config import active_config
        
        # Log the error
        log_func = getattr(logger, log_level, logger.error)
        
        if isinstance(error, EcommerceException):
            log_func(f"[{error.error_code}] {error.message}", extra={'details': error.details})
            user_msg = user_message or error.message
        else:
            log_func(f"Unexpected error: {str(error)}", exc_info=True)
            user_msg = user_message or "An unexpected error occurred. Please try again later."
        
        # Display error to user
        if isinstance(error, ValidationError):
            st.warning(f"⚠️ {user_msg}")
        elif isinstance(error, AuthenticationError):
            st.error(f"🔐 {user_msg}")
        elif isinstance(error, PaymentError):
            st.error(f"💳 {user_msg}")
        elif isinstance(error, ProductNotFoundError):
            st.error(f"🔍 {user_msg}")
        elif isinstance(error, InsufficientStockError):
            st.warning(f"📦 {user_msg}")
        else:
            st.error(f"❌ {user_msg}")
        
        # Show details in debug mode
        if active_config.DEBUG and show_details_in_debug:
            with st.expander("🔧 Error Details (Debug Mode)"):
                st.code(str(error))
                if isinstance(error, EcommerceException) and error.details:
                    st.json(error.details)
    
    @staticmethod
    def safe_execute(func, *args, error_message: Optional[str] = None, default_return=None, **kwargs):
        """
        Execute a function safely with error handling.
        
        Args:
            func: Function to execute
            *args: Positional arguments for the function
            error_message: Optional error message to display
            default_return: Value to return if an error occurs
            **kwargs: Keyword arguments for the function
            
        Returns:
            Function result or default_return if an error occurs
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            ErrorHandler.handle_error(e, user_message=error_message)
            return default_return


# Example usage:
# from utils.error_handler import ErrorHandler, ValidationError
#
# try:
#     if not email:
#         raise ValidationError("Email is required", field="email")
# except Exception as e:
#     ErrorHandler.handle_error(e)
