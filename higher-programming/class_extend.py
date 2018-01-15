class Parent:
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性:",Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")
    def childMethod(self):
        print("调用子类方法")
"""issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
isinstance(obj, Class) 布尔函数如果 obj 是 Class 类的实例对象或者是一个 Class 子类的实例对象则返回 true。"""
# 方法重载
class Animal:
    def myMethod(self):
        print("调用父类方法")
class Dog(Animal):
    def myMethod(self):
        print("调用子类方法")

"""__init__ (self [,args...] )
构造函数
简单的调用方法: obj = className(args)
2	__del__(self)
析构方法, 删除一个对象
简单的调用方法 : del obj
3	__repr__(self)
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__(self)
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ (self, x)
对象比较
简单的调用方法 : cmp(obj, x)"""
# 运算符重载
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d,%d)' %(self.a,self.b)
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

"""类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
在类内部的方法中使用时 self.__private_attrs。"""
class JustCounter:
    # 私有变量
    __secertcount = 0
    # 公开变量
    publicCount = 0
    def count(self):
        self.__secertcount+=1
        self.publicCount+=1
        print(self.__secertcount)
if __name__ == '__main__':
    # c = Child()
    # c.childMethod()
    # c.parentMethod()
    # c.setAttr(200)
    # c.getAttr()
    # dog = Dog()
    # dog.myMethod()
    # v1 = Vector(2,10)
    # v2 = Vector(5,-2)
    # print(v1+v2)
    counter = JustCounter()
    counter.count()
    counter.count()
    print(counter.publicCount)
    # 报错，无法访问类的私有变量
    # print(counter.__secretCount)
#     Python 不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
    print(counter._JustCounter__secretCount)
