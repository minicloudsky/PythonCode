#coding: utf-8
import sys
while True:
    num = sys.stdin.readline()
    if num=="":
        break
    c = []
    for i in range(int(num)):
        b = sys.stdin.readline()
        c.append(int(b))
    c = list(set(c))
    c.sort()
    for i in c:
        print (i)
