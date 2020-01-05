words = ['a', 'b', 'c', 'd', 'e']
dict = {'name': 'zz', 'age': 'dd', 'cc': 'ww'}

# 在遍历同一个集合时修改该集合的代码可能很难获得正确的结果。
# 通常，更直接的做法是循环遍历该集合的副本或创建新集合
# for key, value in dict.copy().items():
# #     if value == 'dd':
# #         del dict[key]
# for key, value in dict.copy().items():
#     if key == 'cc':
#         dict[key] = '111'
#
# print(dict)
# nums = range(5, 10)
# print(sum(nums))
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n // x)
#             break
#     else:
#         print(n, 'is a prime number')
# iloveyou = 9
# while iloveyou:
#     pass


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b, = b, a + b
#     print()
#
# ff= fib
# print(ff(100000000))

# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a + b
#     return result
#
#
# f100 = fib2(100)
# print(f100)
"""
 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。
 比如，下面的函数会存储在后续调用中传递给它的参数
"""


# def f(a, L=[]):
#     L.append(a)
#     return L
#
#
# print(f(1))
# print(f(2))
# print(f(3))
# def foo(name, /, **kwds):
#     return 'name' in kwds
#
#
# print(foo(1, **{'name': 2}))
# 任意的参数列表
# def avg(a, b, *args):
#     return (a + b + sum(args)) / (len(args) + 2)
#
#
# print(avg(1, 2, 3, 4, 5, 6, 7, 8))
# def concat(*args, sep="/"):
#     return sep.join(args)


# print(concat('a', 'b', 'c'))
# print(concat('a', 'b', 'c', sep='xxx'))
# print(list(range(1, 9)))
# args = [3, 6]
# print(list(range(*args)))
# def parrot(voltage, state='a stiff', action='voom'):
#     print("this parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
#
#
# d = {'voltage': 'four', 'state': 'bleedin', 'action': 'get'}
# print(parrot(**d))
#
# def make_incrementor(n):
#     return lambda x: x + n
#
#
# f = make_incrementor(42)
# print(f(0))
# print(f(1))
# 文档字符串
# def my_function():
#     """
#     Do nothing,but document it.
#     :return:
#     """
#     pass
#
#
# print(my_function.__doc__)
def f(ham: str, eggs: str = 'eggs') -> str:
    print("annotations:", f.__annotations__)
    print("arguments: ", ham, eggs)
    return ham + ' and ' + eggs


print(f('spam'))
