#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, unicode_literals
from celery import Celery
app = Celery(
    broker = 'amqp://user:123456@39.105.154.2/test',
    backend='redis://39.105.154.2',
    include=[]
)

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()

