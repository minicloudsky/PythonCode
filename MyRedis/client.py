#coding:utf-8
import redis
r = redis.Redis(host='localhost',port=6379,password='redis')
r.set('github','github')
print(r.keys('*'))
