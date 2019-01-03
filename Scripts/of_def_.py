#!/usr/bin/env python
# @author=huangwl

"""
def sum_():
    n = 123
    n += 1
    print(n)

sum_()
s = sum_
s()



无参数
show():  --> show()

一个参数
def show(arg):
    print(arg)
show('kkk')

两个参数
def show(arg,xxx)
    print(arg,xxx)
show('kkk','777')

默认参数必须放在最后
def show(a1,a2=999)
    print(a1,a2)
# show(666)
show(666,555)

指定参数
def show(a1,a2)
    print(a1,a2)
show(a1=999,a2=666)

动态参数
def show(*arg):
    print(arg,type(arg))        #元祖
show(1,22,33,44)

def show(**arg):
    print(arg,type(arg))        #字典
show(n1=78,n2=22)


def show(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

show(11,22,33,n1=88)


def show(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))
x = [11,22,33,44]
y = {'n1':88,'n2':'huangwl'}
show(*x,**y)

动态参数
s1 = "{0} is {1}"
ret = s1.format('alex','sb')
print(ret)

s1 = "{0} is {1}"
s2 = ['alex','sb']
ret = s1.format(*s2)
print(ret)


s1 = "{name} is {act}"
d = {"name":'huang','act':'welai'}
ret = s1.format(name='huangwl',act='me')
res = s1.format(**d)
print(ret)
print(res)
"""
