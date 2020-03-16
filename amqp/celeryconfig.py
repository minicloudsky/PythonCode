#!/usr/bin/env python
# coding=utf-8

# Celery config

broker_url = 'pyamqp://'

# rabbitmq作为中间人（broker）
# broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'

result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

