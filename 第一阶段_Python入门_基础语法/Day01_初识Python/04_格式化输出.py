# -*- coding: utf-8 -*-
# @Time    : 2025/9/19 10:14
# @File    : 04_格式化输出.py
# @Software: PyCharm

# 格式化输出
name = 'ljk'
age = 33
weight = 78.86
stu_id = 1
# 写法一：
print('---------------写法一---------------------')
print('我的名字是:%s' % name)
print('我的年龄为:%d岁' % age)
print("我的体重为:%.2f公斤" % weight)
print("我的学号是:%03d" % stu_id)  # 以0补全
# 写法二：
print('----------------写法二--------------------')
print('%s的年龄为:%d岁,体重为:%.2f公斤,学号是:%06d' % (name, age, weight, stu_id))#%06d:以0补全,占位符
print('%s明年的年龄为:%d岁' % (name, age + 1))
# 写法三：
print('----------------写法三--------------------')
print(f'我的名字是{name},今年{age}岁了,明年{age+1}岁！')
