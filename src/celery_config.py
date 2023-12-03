from celery import Celery

from config import REDIS_HOST, REDIS_PORT

celery_app = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')