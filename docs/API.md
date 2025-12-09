# API Documentation

This document provides comprehensive API documentation for the SAVA E-Commerce Platform internal modules.

## Table of Contents

- [Configuration (`config.py`)](#configuration)
- [Services](#services)
  - [Firebase Service](#firebase-service)
  - [Authentication Service](#authentication-service)
- [Utilities](#utilities)
  - [Error Handling](#error-handling)
  - [Logging](#logging)
  - [Validators](#validators)
  - [Formatters](#formatters)
- [Components](#components)

---

## Configuration

### `config.py`

Environment-based configuration management.

#### Classes

**`Config`**
Base configuration class with common settings.

**`DevelopmentConfig`**
Development environment configuration (DEBUG enabled).

**`ProductionConfig`**
Production environment configuration (security hardened).

**`TestingConfig`**
Testing environment configuration.

#### Functions

```python
def get_config(env: Optional[str] = None) -> Type[Config]
```
Get configuration class based on environment.

**Parameters:**
- `env` (str, optional): Environment name ('development', 'production', 'testing')

**Returns:**
- Configuration class for the specified environment

**Example:**
```python
from config import get_config

config = get_config('development')
print(config.APP_NAME)  # "SAVA E-Commerce Platform"
```

---

## Services

### Firebase Service

Located in `services/firebase_service.py`

Provides all Firebase operations including authentication, database, and storage.

#### Key Methods

**Product Management**
```python
def get_products(limit: int = 24, category: Optional[str] = None, 
                search_query: Optional[str] = None) -> list
```
Retrieve products with optional filtering.

**Cart Operations**
```python
def add_to_cart(user_id: str, product_id: str, quantity: int) -> bool
def get_user_cart(user_id: str) -> list
def update_cart_item(user_id: str, product_id: str, quantity: int) -> bool
```

**Order Management**
```python
def create_order(user_id: str, cart_items: list, shipping_info: dict, 
                payment_info: dict) -> Optional[str]
def get_user_orders(user_id: str) -> list
```

---

### Authentication Service

Located in `services/auth_service.py`

Handles user authentication and authorization.

---

## Utilities

### Error Handling

Located in `utils/error_handler.py`

#### Custom Exceptions

All exceptions inherit from `EcommerceException`:

**`AuthenticationError`**
- Raised when authentication fails
- Error code: `AUTH_ERROR`

**`ValidationError`**
- Raised when input validation fails
- Error code: `VALIDATION_ERROR`
- Additional field: `field` (name of the invalid field)

**`DatabaseError`**
- Raised when database operations fail
- Error code: `DB_ERROR`

**`PaymentError`**
- Raised when payment processing fails
- Error code: `PAYMENT_ERROR`

**`ProductNotFoundError`**
- Raised when a product is not found
- Error code: `PRODUCT_NOT_FOUND`
- Additional field: `product_id`

**`InsufficientStockError`**
- Raised when there is insufficient stock
- Error code: `INSUFFICIENT_STOCK`
- Additional fields: `product_id`, `requested`, `available`

**`CartError`**
- Raised when cart operations fail
- Error code: `CART_ERROR`

**`ConfigurationError`**
- Raised when configuration is invalid
- Error code: `CONFIG_ERROR`

#### ErrorHandler Class

```python
class ErrorHandler:
    @staticmethod
    def handle_error(error: Exception, user_message: Optional[str] = None, 
                    show_details_in_debug: bool = True, log_level: str = "error")
```

Handle an error by logging it and displaying an appropriate message.

**Parameters:**
- `error`: The exception that occurred
- `user_message`: Optional user-friendly message
- `show_details_in_debug`: Whether to show error details in debug mode
- `log_level`: Logging level ('error', 'warning', 'info')

**Example:**
```python
from utils.error_handler import ErrorHandler, ValidationError

try:
    if not email:
        raise ValidationError("Email is required", field="email")
except Exception as e:
    ErrorHandler.handle_error(e)
```

```python
@staticmethod
def safe_execute(func, *args, error_message: Optional[str] = None, 
                default_return=None, **kwargs)
```

Execute a function safely with error handling.

**Example:**
```python
result = ErrorHandler.safe_execute(
    risky_function, 
    arg1, 
    arg2, 
    error_message="Operation failed",
    default_return=[]
)
```

---

### Logging

Located in `utils/logger.py`

#### Functions

```python
def get_logger(name: str) -> logging.Logger
```

Get a configured logger instance.

**Parameters:**
- `name`: Logger name (typically `__name__` from the calling module)

**Returns:**
- Configured logger with console and file handlers

**Example:**
```python
from utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Application started")
logger.error("An error occurred", exc_info=True)
```

---

### Validators

Located in `utils/validators.py`

Collection of validation functions for user inputs.

#### Functions

**Email Validation**
```python
def validate_email(email: str) -> bool
```

**Password Validation**
```python
def validate_password(password: str, min_length: int = 8) -> tuple[bool, str]
```
Returns `(is_valid, error_message)`

**Phone Validation**
```python
def validate_phone(phone: str) -> bool
```

**Credit Card Validation**
```python
def validate_credit_card(card_number: str) -> bool
```

---

### Formatters

Located in `utils/formatters.py`

Data formatting utilities.

#### Functions

**Currency Formatting**
```python
def format_currency(amount: float, currency: str = "USD") -> str
```

**Date Formatting**
```python
def format_date(date: Union[str, datetime], format: str = "%Y-%m-%d") -> str
```

**Total Calculation**
```python
def calculate_total(cart_items: list, tax_rate: float = 0.08, 
                   shipping: float = 5.99) -> dict
```

Returns a dictionary with:
```python
{
    'subtotal': float,
    'tax': float,
    'shipping': float,
    'total': float
}
```

---

## Components

UI components are located in the `components/` directory.

### Product Card

**File:** `components/product_card.py`

```python
def render_product_card(product: dict, on_click: Optional[callable] = None)
```

Renders a product card with image, name, price, and rating.

### Product List

**File:** `components/product_list.py`

```python
def render_product_grid(products: list, columns: int = 4)
```

Renders products in a responsive grid layout.

### Authentication

**File:** `components/auth.py`

```python
def render_login_form()
def render_register_form()
```

Authentication forms with validation and error handling.

### Cart Summary

**File:** `components/cart_summary.py`

```python
def render_cart_summary(cart_items: list, show_checkout: bool = True)
```

Displays cart summary with totals and checkout button.

### Checkout Form

**File:** `components/checkout_form.py`

```python
def render_checkout_form(cart_items: list)
```

Multi-step checkout form with shipping and payment information.

---

## Error Handling Best Practices

1. **Use specific exceptions** - Choose the most appropriate exception type
2. **Provide context** - Include relevant details in exception messages
3. **Log errors** - All errors are automatically logged
4. **User-friendly messages** - Display clear messages to users
5. **Debug mode** - Additional details shown in development

**Example:**
```python
from utils.error_handler import ErrorHandler, ProductNotFoundError
from utils.logger import get_logger

logger = get_logger(__name__)

def get_product(product_id: str):
    try:
        product = firebase.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError(product_id)
        return product
    except Exception as e:
        ErrorHandler.handle_error(e, user_message="Unable to load product")
        return None
```

---

## Configuration Variables

See `.env.example` for all available configuration variables.

### Required Variables

- `SECRET_KEY` - Application secret key (min 32 characters)
- `FIREBASE_SERVICE_ACCOUNT_PATH` - Path to Firebase credentials
- `FIREBASE_DATABASE_URL` - Firebase database URL

### Optional Variables

- `LOG_LEVEL` - Logging level (DEBUG, INFO, WARNING, ERROR)
- `DEFAULT_TAX_RATE` - Tax rate for orders (default: 0.08)
- `DEFAULT_SHIPPING_COST` - Shipping cost (default: 5.99)
- `PRODUCTS_PER_PAGE` - Pagination size (default: 24)

---

## Testing

All modules include comprehensive unit tests in the `tests/` directory.

**Run tests:**
```bash
pytest
pytest --cov  # With coverage
pytest tests/test_config.py  # Specific file
```

**Test fixtures** are available in `tests/conftest.py` for common test data.

---

For more information, see the [README](README.md) and [Contributing Guidelines](CONTRIBUTING.md).
