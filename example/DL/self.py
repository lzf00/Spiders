# -*- codeing = utf-8 -*-
# @Time : 2021/10/30 16:22
# @Author : lzf
# @File : self.py
# @Software :PyCharm
# class Person(object):
#     def _init_(self,name):
#         self.name=name
#     def sayhello(self):
#         print ('My name is:',self.name)
# object='bill'
# p1=Person(object)
# p2 = Person('Apple')
# print (p1)

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def sayhello(self):
#         print ('My name is:',self.name)
# p=Person('Bill')
# print (p)

# class Test(object):
#     def __init__ (self, val1):
#         self.val0 = val1
#     def fun1(self):
#         print(self.val0)
#     def fun2(self, val2):
#         print(val2)
#     def fun3(self):
#         print(self.fun1)
#         self.fun1()
#
# ins=Test(123)
# ins.new_val="I’m a new value" # 在实例中添加数据属性
# print(ins)
# print(ins.fun3())

a = 1
def say():
    print ('调用了全局方法'  )
class people:
    a = 100
    def say(self):
        print ('调用了类的方法'  )
    def do(self):
        say()
        self.say()
        print( 'a = ' , a  )
        print ('self.a = ' , self.a  )
p = people()
p.do()

