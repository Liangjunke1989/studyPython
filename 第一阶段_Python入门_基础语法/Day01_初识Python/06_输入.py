# -*- coding: utf-8 -*-
# input 模块，获取用户输入，输入的字符串类型是str
# input具有阻塞代码的能力
password = input("请输入用户名：")
print(f'您输入的用户名是:{password}')
print('您输入的用户名的类型是:%s' % type(password))

age='123'
age = int(age)
print(f'您输入的age是:{age}')
print('您输入的age是:%04d' %age)
print('您输入的age的类型是:%s' % type(age))