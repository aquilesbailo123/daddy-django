# Core App

## Purpose

The Core app serves as the foundation of the Daddy Django project, providing shared functionality, templates, and base components that can be used throughout the application.

## Features

- **Base Models**: Contains abstract base models (`BaseModel`, `UserMixinModel`) that provide common fields and behavior for other models
- **Shared Templates**: Houses the main template structure used across the project
- **Template Tags**: Custom template tags for various functionalities including:
  - Language switching (`change_lang.py`)
  - Environment variable access (`env_tags.py`)
  - Domain getting (`get_domain.py`)
  - Math filters (`mathfilters.py`)
  - String formatting (`spacecomma.py`)
- **Middleware**: Contains custom middleware classes for request/response processing
- **Core Exceptions**: Defines custom exceptions for use throughout the application

## Structure

```
core/
├── migrations/         # Database migrations
├── templates/          # Shared templates
│   ├── account/        # Authentication-related templates
│   ├── accounts/       # Account management templates
│   ├── admin/          # Admin customization templates
│   └── base_layout.html # Base email template
├── templatetags/       # Custom template tags
├── admin.py            # Admin site registrations
├── apps.py             # App configuration
├── exceptions.py       # Custom exceptions
├── middleware.py       # Custom middleware
├── models.py           # Abstract base models
└── views.py            # Core views
```

## Usage

The Core app should be used for functionality that is shared across multiple apps in the project. When building new features:

1. Consider if the functionality belongs in a specific domain app or if it's general enough to be part of Core
2. Use the abstract models as base classes for your domain models to maintain consistency
3. Extend the template system by adding new templates within the appropriate directories
4. Add new templatetags as needed for view-specific formatting and logic

## Extending

When extending the Core app:

1. Keep the focus on shared functionality
2. Maintain backwards compatibility with existing components
3. Document any new abstract models or base classes
4. Add tests for any new functionality
