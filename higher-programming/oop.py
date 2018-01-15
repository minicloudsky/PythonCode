#-*- coding: utf-8 -*-
class Employee:
    '所有员工的基类'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ",self.name,",Salary: ",self.salary)

class Test:
    def prt(s):
        print(s)
        print(s.__class__)

"""Python 内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ : 类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块 mymod 中，
那么 className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）"""
if __name__ == '__main__':
    # t = Test()
    # t.prt()
    emp1 = Employee("zara",2000)
    emp2 = Employee("Manni",5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print("Total Employee %d" %Employee.empCount)
    emp1.salary=1000
    emp2.empCount = 100
    print(emp1.salary)
    print(emp2.empCount)
    # 访问对象的属性
    print(hasattr(emp1,'age'))
    # 检查是否存在一个属性
    hasattr(emp2,'age')
    # 设置一个属性，如果属性不存在，会创建一个新属性
    setattr(emp1,'age',8)
    # 删除一个属性
    delattr(emp1,'age')
    print("Employee.__doc__ ：",Employee.__doc__)
    print("Employee.__name__ :",Employee.__name__)
    print("Employee.__module__ :",Employee.__module__)
    print("Employee.__bases__ :",Employee.__bases__)
    print("Employee.__dict__ :",Employee.__dict__)