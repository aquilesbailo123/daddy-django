# Users App

## Purpose

The Users app handles all aspects of user management, authentication, and security in the Daddy Django project. It provides a comprehensive authentication system that extends Django's default capabilities with additional security features and user profile management.

## Features

- **Authentication System**: Built on dj-rest-auth and allauth with customizations
- **User Profile**: Extended user model with additional information and security settings
- **Login History**: Tracking of login attempts with IP and device information
- **Security Features**: 
  - Action freezing for suspicious activities
  - IP change detection with notifications
  - Captcha integration for sensitive operations
  - Email verification workflows
- **REST API Endpoints**: Authentication-related API endpoints with proper serializers
- **Custom Adapters**: Adapters for third-party authentication services
- **Password Management**: Secure password reset and change workflows

## Structure

```
users/
├── auth/                # Authentication-related components
│   ├── adapters.py      # Adapters for authentication services
│   └── backends.py      # Custom authentication backends
├── migrations/          # Database migrations
├── serializers/         # API serializers
│   ├── auth.py          # Authentication serializers
│   └── profile.py       # User profile serializers
├── admin.py             # Admin site registrations
├── apps.py              # App configuration
├── cache_keys.py        # Cache key definitions
├── captcha.py           # Captcha handling
├── exceptions.py        # Custom exceptions
├── models.py            # User-related models
├── signals.py           # Signal handlers
├── tasks.py             # Asynchronous tasks
├── urls.py              # URL configurations
├── utils.py             # Utility functions
└── views.py             # Authentication views
```

## Key Components

### Models

- **Profile**: Extends the User model with additional fields and security methods
- **LoginHistory**: Records login attempts with context information

### Authentication Flow

1. User registration with email verification
2. Login with security checks (IP tracking, captcha)
3. Password management (reset, change) with security measures
4. Optional two-factor authentication infrastructure

### Security Measures

- IP change detection sends notifications to users
- Account action freezing after sensitive operations
- Login history tracking for security auditing
- Captcha validation for sensitive operations

## Extending

When extending the Users app:

1. Use the existing authentication flow as much as possible
2. Extend the Profile model for additional user information
3. Add new serializers in the appropriate directory
4. Implement additional security measures as needed

## Integration

The Users app is designed to be the central authentication system for the entire project. New apps should:

1. Use the Profile model for user-related information
2. Leverage the authentication system for securing endpoints
3. Follow the established security patterns
