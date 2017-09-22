from __future__ import absolute_import, unicode_literals
from .celery import app

@app.task
def task(string):
    # import rpdb; rpdb.set_trace()
    return string
