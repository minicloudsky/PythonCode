#!/usr/bin/env python
# coding=utf-8
from celery import Celery

app = Celery('tasks', broker='amqp://user:123456@39.105.154.2/test', backend='redis://39.105.154.2')

app.conf.task_serializer = 'json'

@app.task
def add(x, y):
        return x + y

@app.task
def mul(x,y):
    return x*y

@app.task
def xsum(numbers):
    return sum(numbers)




if __name__ == '__main__':
    add(1,2)
