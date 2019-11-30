#coding: utf-8
import random
def select(list):
    length = len(list)
    for i in range(0,length-1):
        for j in range(i,length):
            if(list[i]>list[j]):
                list[i],list[j] = list[j],list[i]
    return list
list = []
n = int(input())
for i in range(1,n+1):
    tmp = int(input())
    list.append(tmp)
list.sort()
list = set(list)
list = select(list)
for i in list :
    print(i)
