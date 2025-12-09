"""
Unit tests for the error handler module.
"""
import pytest
from utils.error_handler import (
    EcommerceException,
    AuthenticationError,
    ValidationError,
    DatabaseError,
    PaymentError,
    ProductNotFoundError,
    InsufficientStockError,
    CartError,
    ConfigurationError,
    ErrorHandler
)


class TestExceptions:
    """Test custom exception classes."""
    
    def test_ecommerce_exception(self):
        """Test base EcommerceException."""
        exc = EcommerceException("Test error", error_code="TEST_ERROR")
        assert str(exc) == "Test error"
        assert exc.error_code == "TEST_ERROR"
        assert exc.details == {}
    
    def test_ecommerce_exception_with_details(self):
        """Test EcommerceException with details."""
        details = {"field": "email", "value": "invalid"}
        exc = EcommerceException("Invalid email", details=details)
        assert exc.details == details
    
    def test_authentication_error(self):
        """Test AuthenticationError."""
        exc = AuthenticationError()
        assert exc.error_code == "AUTH_ERROR"
        assert "Authentication failed" in str(exc)
    
    def test_validation_error(self):
        """Test ValidationError."""
        exc = ValidationError("Email is required", field="email")
        assert exc.error_code == "VALIDATION_ERROR"
        assert exc.details['field'] == "email"
    
    def test_database_error(self):
        """Test DatabaseError."""
        exc = DatabaseError()
        assert exc.error_code == "DB_ERROR"
    
    def test_payment_error(self):
        """Test PaymentError."""
        exc = PaymentError()
        assert exc.error_code == "PAYMENT_ERROR"
    
    def test_product_not_found_error(self):
        """Test ProductNotFoundError."""
        exc = ProductNotFoundError("prod_123")
        assert exc.error_code == "PRODUCT_NOT_FOUND"
        assert exc.details['product_id'] == "prod_123"
        assert "prod_123" in str(exc)
    
    def test_insufficient_stock_error(self):
        """Test InsufficientStockError."""
        exc = InsufficientStockError("prod_456", requested=10, available=5)
        assert exc.error_code == "INSUFFICIENT_STOCK"
        assert exc.details['product_id'] == "prod_456"
        assert exc.details['requested'] == 10
        assert exc.details['available'] == 5
    
    def test_cart_error(self):
        """Test CartError."""
        exc = CartError()
        assert exc.error_code == "CART_ERROR"
    
    def test_configuration_error(self):
        """Test ConfigurationError."""
        exc = ConfigurationError()
        assert exc.error_code == "CONFIG_ERROR"


class TestErrorHandler:
    """Test ErrorHandler class."""
    
    def test_safe_execute_success(self):
        """Test safe_execute with successful function."""
        def success_func(x, y):
            return x + y
        
        result = ErrorHandler.safe_execute(success_func, 2, 3)
        assert result == 5
    
    def test_safe_execute_with_exception(self):
        """Test safe_execute with function that raises exception."""
        def failing_func():
            raise ValueError("Test error")
        
        result = ErrorHandler.safe_execute(failing_func, default_return="default")
        assert result == "default"
    
    def test_safe_execute_with_kwargs(self):
        """Test safe_execute with keyword arguments."""
        def func_with_kwargs(a, b=10):
            return a * b
        
        result = ErrorHandler.safe_execute(func_with_kwargs, 5, b=3)
        assert result == 15
    
    def test_safe_execute_returns_none_by_default(self):
        """Test that safe_execute returns None by default on error."""
        def failing_func():
            raise Exception("Error")
        
        result = ErrorHandler.safe_execute(failing_func)
        assert result is None
