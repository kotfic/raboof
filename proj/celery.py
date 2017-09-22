from __future__ import absolute_import, unicode_literals
from setuptools import setup
from celery import Celery
from .serializer import serialize, deserialize
from kombu.serialization import register, registry

# Register the custom serializer with kombu
register('reverse', serialize, deserialize,
         content_type='application/json',
         content_encoding='utf-8')

app = Celery('proj',
             broker='amqp://',
             backend='amqp://',
             include=['proj.tasks'])

app.conf.update(
    accept_content=['reverse'],
    result_expires=3600,
    task_serializer='reverse',
    result_serializer='reverse',
)

if __name__ == '__main__':
    app.start()
