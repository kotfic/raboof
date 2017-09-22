from __future__ import absolute_import, unicode_literals
from .celery import app

@app.task
def task(option, str1):
    print(str1)
