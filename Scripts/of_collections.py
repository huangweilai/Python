#!/usr/bin/env python
# @author=huangwl

import collections


# Counter 计数器
"""
obj = collections.Counter('hahduawhuhuiuieywa')
print(obj.most_common(4))                   #获取出现最多的4个
print(obj)

for k in obj.elements():
    print(k)            #获取key

for k,v in obj.items():
    print(k,v)
    

obj = collections.Counter(['11','22','22','33'])
print(obj)
obj.update(['huangwl','22','33'])
print(obj)
obj.subtract(['huangwl'])
print(obj)

"""

# oraderedDict有序字典
"""
dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
dic['k4'] = None

dic.setdefault('k5',66)
# dic.move_to_end('k1')
print(dic)
dic.popitem()
print(dic)
ret = dic.pop('k2')             #获取返回值
print(dic)
print(ret)
dic.update({'k1':'123','k10':'v10'})
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
"""

# defualtDict默认字典
"""
dic = collections.defaultdict(list)
dic['k1'].append('huangwl')
print(dic)
"""

"""
将以下集合中大于66的值保存至字典的第一个key中，小于或等于66的保持至第二个key中。
[11,22,33,44,55,66,77,88,99]
{'k1': >66,'k2': <=66}
"""

"""
my_list = [11,22,33,44,55,66,77,88,99]
my_dic = {}
my_dic = collections.defaultdict(list)

for v in my_list:
    if v>66:
        my_dic['k1'].append(v)
    else:
        my_dic['k2'].append(v)
print(my_dic)

# namedtuple可命名元祖

mytupleClass = collections.namedtuple('mytupleClass',['x','y','z'])
obj = mytupleClass(11,22,33)
print(obj.x)
print(obj.y)
print(obj.z)
"""

# 双向队列deque
"""
d = collections.deque()
d.append('1')           #添加
d.appendleft('10')      #从左添加
d.appendleft('1')
print(d)
r = d.count('1')
print(r)
d.extend(['hh','ww','ll'])        #从右边扩展
d.extendleft(['qq','ww','ee'])    #从左扩展
d.reverse()
d.rotate(1)                     #从队列的尾部抓取数据放到首位
print(d)
"""


# 单向队列queue.Queue
import queue
q = queue.Queue()
q.put('123')
print(q.qsize())            #获取元素个数
print(q.get())              #获取数据
