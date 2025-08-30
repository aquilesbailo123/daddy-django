# Google Cloud Services custom settings

from .env import env

GCS_BUCKET_NAME = env('GCS_BUCKET_NAME', default='')
GCS_CREDENTIALS_PATH = env('GCS_CREDENTIALS_PATH', default='')
GCS_PROJECT_ID = env('GCS_PROJECT_ID', default='')