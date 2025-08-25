from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DEFAULT_RENDERER_CLASSES': (
        # we can add a custom json encoder here
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/second',
        'user': '10/second',
        'dj_rest_auth': '10/second',
    },
    # 'EXCEPTION_HANDLER': 'we can add a custom exception handler',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# These are the settings for dj-rest-auth with simplejwt
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt_auth_token',
    'JWT_AUTH_REFRESH_COOKIE': 'jwt_refresh_token',
    'JWT_EXPIRATION_DELTA': timedelta(minutes=60),
    'JWT_AUTH_RETURN_EXPIRATION': True,
    'TOKEN_MODEL': None,
    'JWT_AUTH_HTTPONLY': False,  # When False, allows JavaScript to access cookies + ensures refresh token in JSON response
    'EMAIL_VERIFICATION': True,

    'USER_DETAILS_SERIALIZER': 'users.serializers.auth.UserSerializer',
    
    # This setting prevents tokens from being issued during registration
    'TOKEN_SERIALIZER': None,
    'LOGIN_SERIALIZER': 'users.serializers.auth.LoginSerializer',
    'REGISTER_SERIALIZER': 'users.serializers.auth.RegisterSerializer',

    'PASSWORD_RESET_SERIALIZER': 'users.serializers.auth.PasswordResetSerializer',
    'PASSWORD_CHANGE_SERIALIZER': 'users.serializers.auth.PasswdChangeSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'users.serializers.auth.PasswordResetConfirmSerializer',

    # 'JWT_AUTH_COOKIE_USE_CSRF': False, # To not need CSRF token
    # 'OLD_PASSWORD_FIELD_ENABLED': True, # To allow old password field in change password serializer
    'JWT_AUTH_SECURE': False, # To allow cookies to be sent over HTTP TODO CHECK
}

OLD_PASSWORD_FIELD_ENABLED = True

# JWT settings (if you're using JWT)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5), 
    'ROTATE_REFRESH_TOKENS': True,
    'UPDATE_LAST_LOGIN': True,
    'AUTH_HEADER_TYPES': ('Bearer', 'Token',),
    'ALGORITHM': 'HS512'
}



