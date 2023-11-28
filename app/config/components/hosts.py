import os

from dotenv import load_dotenv

load_dotenv()


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(',')

# debug_toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]
