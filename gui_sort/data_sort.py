# -*- coding: utf-8 -*-
import math
import sys
class My_Sort():
    #1插入排序
    def insert_sort(self,lists):
        count = len(lists)
        for i in range(1,count):
            key = lists[i]
            j = i-1
            while j>=0:
                if lists[j] > key:
                    lists[j+1] = lists[j]
                    lists[j] = key
                j-=1
        return lists
    #2希尔排序,python中必须注意，循环中步长为整数
    def shell_sort(self,lists):
        count = int(len(lists))
        step = 2
        group = int(count /step)
        while group >0:
            for i in range(group):
                j = i+group
                while j< count:
                    k = j - group
                    key = lists[j]
                    while(k>=0):
                        if lists[k] >key:
                            lists[k+group] = lists[k]
                            lists[k] = key
                        k -= group
                    j += group
            group = int(group/step)
        return lists
    #3冒泡排序
    def buddle_sort(self,lists):
        count = len(lists)
        for i in range(count):
            for j in range(i+1,count):
                if lists[i] >lists[j]:
                    lists[i],lists[j] = lists[j],lists[i]
        return lists
    #4直接选择排序
    def select_sort(self,lists):
        count = len(lists)
        for i in range(count):
            min = i
            for j in range(i+1,count):
                if lists[min] > lists[j]:
                    min = j
            lists[min],lists[i] = lists[i],lists[min]
        return lists
    #5快速排序
    def quick_sort(self, lists, left, right):
        if left > right:
            return
        i = left
        j = right
        while i != j:
            while lists[j] >= lists[left] and i < j:
                j -= 1
            while lists[i] <= lists[left] and i < j:
                i += 1
            if i < j:
                lists[i], lists[j] = lists[j], lists[i]
        lists[left], lists[i] = lists[i], lists[left]
        self.quick_sort(lists, left, i - 1)
        self.quick_sort(lists, i + 1, right)
        return lists
    #6堆排序
    #调整堆
    def adjust_heap(self,lists,i,size):
        lchild = 2*i+1
        rchild = 2*i+2
        max = i
        if i < int(size/2):
            if lchild < size and lists[lchild] > lists[max]:
                max = lchild
            if rchild < size and lists[rchild] > lists[max]:
                max = rchild
            if max !=i:
                lists[max],lists[i] = lists[i],lists[max]
                self.adjust_heap(lists,max,size)
    # 创建堆
    def build_heap(self,lists,size):
        for i in range(0,int((size/2)))[::-1]:
            self.adjust_heap(lists,i,size)
    #堆排序
    def heap_sort(self,lists):
        size = int(len(lists))
        self.build_heap(lists,size)
        for i in range(0,size)[::-1]:
            lists[0],lists[i] = lists[i], lists[0]
            self.adjust_heap(lists,0,i)
        return lists
    
        
        
   
            
            
            

    
                    
    
        
