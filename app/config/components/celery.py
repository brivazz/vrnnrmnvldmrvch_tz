import os

from dotenv import load_dotenv

load_dotenv()


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')

CELERY_TIMEZONE = os.environ.get('CELERY_TIMEZONE')
CELERY_TASK_TRACK_STARTED = os.environ.get('CELERY_TASK_TRACK_STARTED', False) == 'True'
CELERY_TASK_TIME_LIMIT = os.environ.get('CELERY_TASK_TIME_LIMIT')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = os.environ.get(
    'CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP', False
) == 'True'
