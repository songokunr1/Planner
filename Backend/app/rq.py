from celery import Celery
from time import sleep
from os import environ

# environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

# broker_url = "amqp://localhost"
# redis_url = "redis://localhost"
# broker_url = 'amqp://guest:guest@localhost:5672'
broker_url = "amqp://localhost"
redis_url = "redis://localhost"
broker_url = 'amqp://guest:guest@localhost:5672'

app = Celery('tasks', broker=redis_url, backend=redis_url)
# app.config_from_envvar('CELERY_CONFIG_MODULE')
# app = Celery('tasks', broker=broker_url, backend=redis_url)


@app.task
def say_hello(name: str):
    sleep(5)
    return f"Hello {name}"