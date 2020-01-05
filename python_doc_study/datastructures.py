list = [-12, 12, 54, 6, 656, 7657, 7657, 1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
# list.append(10)
# list.extend(list2)
# list.insert(2, 0)
# list.remove(1) # 移除列表中第一个值为 x 的元素。如果没有这样的元素，则抛出 ValueError 异常。
# list.pop(0)
# list.clear()
# del list[:3]
# print(list.index(3))
# print(list.count(1))
# list.sort()
# print(list)
# list.reverse()
# print(list)
# print(list.copy())
# 列表作为堆栈
stack = [1, 2, 3, 4, 5]
# stack.append(6)
# stack.append(7)
stack.pop()
# print(stack)
# 列表做队列用
from collections import deque

queue = deque(['Eric', 'John', 'Tom'])
queue.append('michael')
# print(queue)
# queue.popleft()
# print(queue)
# 列表推导式
# squares = []
# for x in range(10):
#     squares.append(x ** 2)
# print(squares)
# squares = list(map(lambda x: x ** 2, range(10)))
# print(squares)
# squares = [x ** 2 for x in range(10)]
# print(squares)
# combine = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(combine)
