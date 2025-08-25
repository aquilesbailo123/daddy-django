import logging
import os

from .common import DEBUG


ORDERBOOK_LOG_LEVEL = logging.DEBUG

ENVIRONMENT = 'local'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'static_fields': {
            '()': 'backend.loggers.StaticFieldFilter',
            'fields': {
                'project': 'backend',
                'environment': ENVIRONMENT,
            },
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'BitcoinRPC': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'environ': {  
            'handlers': ['console'],
            'level': 'WARNING',  # prevents INFO logs from environ
            'propagate': False,
        },
        'django_otp': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.contrib.auth': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

if DEBUG:
    LOGGING['loggers']['']['level'] = 'DEBUG'
