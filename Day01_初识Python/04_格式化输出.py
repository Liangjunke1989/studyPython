# 格式化输出
name = 'ljk'
age = 33
weight = 78.86
stu_id = 1
print('我的名字是:%s' % name)
print('我的年龄为:%d岁' % age)
print("我的体重为:%.2f公斤" % weight)
print("我的学号是:%03d" % stu_id)  # 以0补全

print('%s的年龄为:%d岁,体重为:%.2f公斤,学号是:%06d' % (name, age, weight, stu_id))

print('%s明年的年龄为:%d岁' % (name, age+1))
