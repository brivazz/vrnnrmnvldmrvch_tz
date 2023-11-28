import os

import pymysql
from dotenv import load_dotenv
pymysql.install_as_MySQLdb()

load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('MYSQL_DB'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
        'PORT': os.environ.get('MYSQL_PORT', 3306),
        'OPTIONS': {
            # для обработки недопустимых или отсутствующих значений,
            # сохраняемых в базе данных операторами INSERT и UPDATE
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
