# 1.float()
num1 = 1
str1 = '10'
res1 = float(num1) + float(str1)
print(res1)  # float和double的区别？
print(type(res1))
# 2.str()
res2 = str(num1) + str(str1)
print(res2)
print(type(res2))
# 3.tuple()   ----将一个序列转换成元组
print("--------------将一个序列转换成元组-----------------")
list1 = [10, 20, 40]
res3 = tuple(list1)
print(res3)
print(type(res3))
# 4.list()    ----将一个序列转换成列表
print("--------------将一个序列转换成列表-----------------")
t1 = (10, 20, 40)
res4 = list(t1)
print(res4)
print(type(res4))
# 5.eval()   -----计算在字符串中的有效Python表达式，并返回一个对象。
#            -----将字符串中的数据转换成它原本的类型
print("--------------eval() 将字符串中的数据转换成它原本的类型-----------------")
str2 = '1'
str3 = '1.1'
str4 = '(10,20,30)'
str5 = '[100,200,300]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

