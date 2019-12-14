#!/usr/bin/env python
# coding=utf-8
def drop_first_last(grades):
    first,*middle,last = grades
    return avg(middle)

if __name__=='__main__':
    grades = [1,2,3,4,5]
    result = drop_first_last(grades)
    print(result)
