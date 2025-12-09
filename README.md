# SAVA E-Commerce Platform 🛍️

> A modern, scalable e-commerce platform built with Streamlit, Firebase, and Python. Featuring a clean design inspired by MercadoLibre with comprehensive security and testing.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit]( https://img.shields.io/badge/Streamlit-1.29+-red.svg)](https://streamlit.io)
[![Firebase](https://img.shields.io/badge/Firebase-Latest-orange.svg)](https://firebase.google.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ Features

### Core Functionality
- 🛒 **Product Catalog** - Browse, search, and filter products
- 🛍️ **Shopping Cart** - Add, update, and manage cart items
- 💳 **Secure Checkout** - Complete purchase with shipping and tax calculation
- 👤 **User Authentication** - Sign up, sign in, and account management
- 📦 **Order Tracking** - View order history and status
- 🔍 **Advanced Search** - Search products by name, category, and more
- 📱 **Responsive Design** - Optimized for desktop and mobile

### Technical Features
- 🔒 **Security** - Environment-based configuration and secure secrets management
- 📝 **Logging** - Centralized logging with file rotation
- ⚠️ **Error Handling** - Comprehensive error handling and user-friendly messages
- 🧪 **Testing** - Unit and integration tests with pytest
- 🚀 **CI/CD** - Automated testing and deployment with GitHub Actions
- 🌐 **Bilingual** - Spanish and English language support

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** Firebase Firestore
- **Authentication:** Firebase Auth
- **Storage:** Firebase Storage
- **Hosting:** Streamlit Cloud

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Git
- Firebase account (free tier works fine)
- Code editor (VS Code recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/GIUSEPPESAN21/New-Software.git
cd New-Software
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

### Firebase Setup

1. Create a Firebase project at https://console.firebase.google.com/

2. Enable the following services:
   - Firestore Database
   - Authentication
   - Storage

3. Generate a service account key:
   - Go to Firebase Console → Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Save the JSON file (DO NOT commit it to Git)

4. Get your Firebase Web API Key (required for authentication):
   - Go to Firebase Console → Project Settings → General
   - Scroll down to "Your apps" section
   - If you don't have a web app, click "Add app" and select Web (</>) icon
   - Copy the "Web API Key" (also called "API Key" or "Browser Key")
   - This key is safe to use in client-side applications

### Streamlit Cloud Deployment

1. Push your code to GitHub

2. Connect your repository to Streamlit Cloud:
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select your repository

3. Configure secrets in Streamlit Cloud:
   - Go to your app settings
   - Click "Secrets"
   - Add the following secrets:

```toml
# Firebase Credentials (from your service account JSON)
[firebase_credentials]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR-KEY\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/..."

# Firebase Web API Key (required for authentication)
firebase_api_key = "your-firebase-web-api-key"

# Gemini API Key (optional)
[gemini]
api_key = "your-gemini-api-key"
# OR use this format:
GEMINI_API_KEY = "your-gemini-api-key"
```

### Local Development

1. Create `.streamlit/secrets.toml` file:
```bash
mkdir -p .streamlit
```

2. Copy your Firebase service account JSON content to `.streamlit/secrets.toml` in the format shown above

3. Run the application:
```bash
streamlit run app.py
```

## 📁 Project Structure

```
ecommerce-platform/
├── app.py                      # Main application entry point
├── config.py                  # Environment configuration
├── requirements.txt           # Python dependencies
├── pyproject.toml            # Development tools configuration
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore patterns
├── CONTRIBUTING.md           # Contributing guidelines
├── CHANGELOG.md              # Version history
├── README.md                 # This file
│
├── components/               # Reusable UI components
│   ├── auth.py              # Authentication forms
│   ├── product_card.py      # Product card display
│   ├── product_list.py      # Product grid layout
│   ├── cart_summary.py      # Cart summary  widget
│   ├── checkout_form.py     # Checkout form
│   └── about.py             # About page content
│
├── services/                 # Business logic layer
│   ├── firebase_service.py  # Firebase operations
│   └── auth_service.py      # Authentication service
│
├── utils/                    # Utility functions
│   ├── validators.py        # Input validation
│   ├── formatters.py        # Data formatting
│   ├── logger.py            # Logging configuration
│   └── error_handler.py     # Error handling
│
├── tests/                    # Test suite
│   ├── conftest.py          # Pytest fixtures
│   ├── test_config.py       # Config tests
│   └── test_error_handler.py # Error handler tests
│
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline
│
├── static/
│   └── uploads/            # User uploads (gitignored)
│
└── logs/                     # Application logs (gitignored)
```

## Firebase Firestore Structure

### Collections

- **users**: User accounts
  - `uid`: User ID
  - `email`: Email address
  - `display_name`: Display name
  - `cart`: Array of cart items
  - `orders`: Array of order IDs
  - `addresses`: Array of addresses
  - `created_at`: Timestamp

- **products**: Product catalog
  - `name`: Product name
  - `description`: Product description
  - `price`: Product price
  - `category`: Product category
  - `images`: Array of image URLs
  - `stock`: Available stock
  - `active`: Boolean (active/inactive)
  - `rating`: Average rating
  - `reviews_count`: Number of reviews
  - `created_at`: Timestamp
  - `updated_at`: Timestamp

- **orders**: Customer orders
  - `user_id`: User ID
  - `items`: Array of order items
  - `totals`: Order totals (subtotal, tax, shipping, total)
  - `shipping_info`: Shipping address
  - `payment_info`: Payment information
  - `status`: Order status (pending, processing, shipped, delivered, cancelled)
  - `created_at`: Timestamp
  - `updated_at`: Timestamp

## Security Rules

Make sure to configure Firebase Security Rules for production:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    match /products/{productId} {
      allow read: if true;
      allow write: if request.auth != null; // Restrict to admins in production
    }
    match /orders/{orderId} {
      allow read, write: if request.auth != null && 
        (resource == null || resource.data.user_id == request.auth.uid);
    }
  }
}
```

## 📖 Usage

### For End Users

1. **Browse Products** - Explore the product catalog on the home page
2. **Search & Filter** - Use search bar and category filters
3. **View Details** - Click on products to see full information
4. **Add to Cart** - Add desired products to your shopping cart
5. **Checkout** - Complete purchase with shipping information
6. **Track Orders** - Monitor order status in your account

### For Developers

#### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest tests/test_config.py
```

#### Code Formatting

```bash
# Format code
black .
isort .

# Check style
flake8 .

# Type checking
mypy .
```

#### Environment Variables

Create a `.env` file based on `.env.example`:

```bash
ENVIRONMENT=development
DEBUG=True
SECRET_KEY=your-secret-key-change-in-production
FIREBASE_SERVICE_ACCOUNT_PATH=path/to/service-account.json
FIREBASE_DATABASE_URL=https://your-project.firebaseio.com
```

## Deployment

This application is designed to run 100% in the cloud on Streamlit Cloud. No local execution is required.

1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Configure secrets
4. Deploy!

## 🔒 Security Best Practices

- Never commit `.env` files or Firebase credentials
- Use environment variables for all sensitive data
- Validate all user inputs
- Keep dependencies updated
- Review security rules regularly
- Use HTTPS in production
- Implement rate limiting for production

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Joseph Javier Sánchez Acuña (GIUSEPPESAN21)**
- GitHub: [@GIUSEPPESAN21](https://github.com/GIUSEPPESAN21)
- LinkedIn: [Joseph Javier Sánchez Acuña](https://www.linkedin.com/in/joseph-javier-sánchez-acuña-150410275)
- Organization: SAVA Software for Engineering

## 🙏 Support

If you find this project helpful, please consider:

- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📖 Improving documentation

For issues and questions, please [open an issue](https://github.com/GIUSEPPESAN21/ecommerce-platform/issues) on GitHub.

## 📚 Additional Documentation

- [Contributing Guidelines](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [API Documentation](#) (Coming soon)

---

© 2025 SAVA Software for Engineering. All rights reserved.
