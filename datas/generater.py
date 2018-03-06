# -*- coding: utf-8 -*-

def fib(max):
    a= 2
    while a< max:
        yield a
        a = a*a

for i in fib(1000):
    print(i)