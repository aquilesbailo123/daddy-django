from .env import env

# TODO do we need this?
# import os
# os.environ.setdefault('C_FORCE_ROOT', 'true')

# Celery
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = [
    'json',
    'pickle',
]

# RabbitMQ broker settings
AMQP_IS_EXTERNAL = env('AMQP_IS_EXTERNAL', default=True)  # Default to external
AMQP_USER = env('AMQP_USER', default='guest')
AMQP_PASS = env('AMQP_PASS', default='guest')
AMQP_HOST = env('AMQP_HOST', default='localhost')
AMQP_PORT = env('AMQP_PORT', default='5672')

# Construct the broker URL
BROKER_URL = f"{'amqps' if AMQP_IS_EXTERNAL else 'amqp'}://{AMQP_USER}:{AMQP_PASS}@{AMQP_HOST}:{AMQP_PORT}/{AMQP_USER if AMQP_IS_EXTERNAL else '/'}"

# # Use RabbitMQ for results as well
# CELERY_RESULT_BACKEND = 'rpc://'

# # Task execution settings
# CELERY_TASK_IGNORE_RESULT = True  # Ignore results unless explicitly configured
# CELERY_TASK_STORE_ERRORS_EVEN_IF_IGNORED = True  # Still log errors

# # Task retry settings
# CELERY_TASK_MAX_RETRIES = 3
# CELERY_TASK_RETRY_DELAY = 5  # 5 seconds

# # External RabbitMQ is used, so we ensure tasks are not run synchronously
# CELERY_TASK_ALWAYS_EAGER = False  # Ensure tasks are run asynchronously with RabbitMQ
# CELERY_TASK_EAGER_PROPAGATES = True  # Propagate exceptions when in eager mode
