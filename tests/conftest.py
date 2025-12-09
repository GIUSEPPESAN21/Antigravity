"""
Test fixtures and configuration for pytest.
"""
import pytest
import sys
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def mock_firebase_user():
    """Mock Firebase user data."""
    return {
        'uid': 'test_user_123',
        'email': 'test@example.com',
        'display_name': 'Test User',
        'email_verified': True
    }


@pytest.fixture
def mock_product():
    """Mock product data."""
    return {
        'id': 'prod_123',
        'name': 'Test Product',
        'description': 'A test product for unit tests',
        'price': 29.99,
        'stock': 100,
        'category': 'Electronics',
        'images': [
            {'url': 'https://example.com/image1.jpg', 'alt': 'Product image 1'}
        ],
        'rating': 4.5,
        'reviews_count': 42
    }


@pytest.fixture
def mock_cart_item():
    """Mock cart item data."""
    return {
        'product_id': 'prod_123',
        'name': 'Test Product',
        'price': 29.99,
        'quantity': 2,
        'image': 'https://example.com/image1.jpg'
    }


@pytest.fixture
def mock_order():
    """Mock order data."""
    return {
        'id': 'order_456',
        'user_id': 'test_user_123',
        'status': 'pending',
        'items': [
            {
                'product_id': 'prod_123',
                'name': 'Test Product',
                'price': 29.99,
                'quantity': 2
            }
        ],
        'totals': {
            'subtotal': 59.98,
            'tax': 4.80,
            'shipping': 5.99,
            'total': 70.77
        },
        'created_at': '2024-01-01T12:00:00Z'
    }


@pytest.fixture(autouse=True)
def reset_environment(monkeypatch):
    """Reset environment variables before each test."""
    monkeypatch.setenv("ENVIRONMENT", "testing")
    monkeypatch.setenv("DEBUG", "True")


@pytest.fixture
def sample_config_values():
    """Sample configuration values for testing."""
    return {
        'SECRET_KEY': 'a' * 64,
        'FIREBASE_DATABASE_URL': 'https://test.firebaseio.com',
        'DEFAULT_TAX_RATE': '0.08',
        'DEFAULT_SHIPPING_COST': '5.99',
    }
