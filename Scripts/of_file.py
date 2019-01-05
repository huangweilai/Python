#!/usr/bin/env python
# @author=huangwl

f = open('2019-01-05.log','w')
f.write('huangwl')
f.close()


f = open('2019-01-05.log','r+')
# print(f.tell())
# ret_f = f.read(1)
# print(f.tell())   #查看当前指针位置
# f.seek(2)           #设置指针位置
# ret_f = f.read()
# print(ret_f)
# f.truncate()          保留指针前的内容，并写入到文件中
print(f.read())
f.seek(4)
print(f.read())
f.close()
