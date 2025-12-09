# Contributing to SAVA E-Commerce Platform

Thank you for your interest in contributing to the SAVA E-Commerce Platform! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. **Fork the repository** to your own GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ecommerce-platform.git
   cd ecommerce-platform
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git
- A code editor (VS Code recommended)

### Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.example`:
   ```bash
   copy .env.example .env  # Windows
   cp .env.example .env    # macOS/Linux
   ```

4. Configure your Firebase credentials (see README.md for details)

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://peps.python.org/pep-0008/) for Python code style:

- Use 4 spaces for indentation (not tabs)
- Maximum line length: 100 characters
- Use meaningful variable and function names
- Add docstrings to all public modules, functions, classes, and methods

### Code Formatting

We use automated formatters to maintain consistent style:

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Check code style with flake8
flake8 .
```

### Type Hints

Use type hints where appropriate to improve code clarity:

```python
def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total price."""
    return price * quantity
```

## Testing

### Running Tests

Run the full test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov
```

Run specific test file:

```bash
pytest tests/test_config.py
```

### Writing Tests

- Write tests for all new features and bug fixes
- Place tests in the `tests/` directory
- Use descriptive test names that explain what is being tested
- Follow the Arrange-Act-Assert pattern

Example:

```python
def test_user_registration():
    """Test that a user can successfully register."""
    # Arrange
    email = "test@example.com"
    password = "secure_password_123"
    
    # Act
    result = register_user(email, password)
    
    # Assert
    assert result.success is True
    assert result.user.email == email
```

## Pull Request Process

1. **Update documentation** if you're changing functionality
2. **Add tests** for new features or bug fixes
3. **Run the test suite** and ensure all tests pass
4. **Run code formatters** (black, isort, flake8)
5. **Update CHANGELOG.md** with a description of your changes
6. **Commit your changes** with a descriptive commit message:
   ```
   feat: Add user profile page
   
   - Created new profile component
   - Added profile editing functionality
   - Updated navigation to include profile link
   ```

### Commit Message Guidelines

Use conventional commits format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

7. **Create a Pull Request**:
   - Provide a clear title and description
   - Reference any related issues
   - Wait for code review and address feedback

### Code Review Process

- All pull requests require at least one approval
- Address all review comments
- Keep pull requests focused and reasonably sized
- Be responsive to feedback and questions

## Questions?

If you have questions or need help, please:

- Open an issue on GitHub
- Contact the maintainers
- Check existing documentation

Thank you for contributing to SAVA E-Commerce Platform! 🎉
