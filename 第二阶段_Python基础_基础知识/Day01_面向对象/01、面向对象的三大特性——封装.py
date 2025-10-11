print("---------------------------1、定义一个class类--------------------------------------")
# 1、定义一个class类
"""
        属性=>变量
        方法=>函数
"""
class Person:
    name = 'ljk'
    age = 18
    height = 1.75
    weight = 80
    is_male = True
    @staticmethod
    def eat():
        print('吃吃吃')
    def sleep(self):
        print(self) #self指向实例化对象
        self.name='juhnko'
        print(f'{self.name}喜欢睡觉')
print("----------------------2、实例化对象-------------------------")
# 2、实例化对象
p1=Person()
print(p1)
print("----------------------3、调用方法---------------------------")
p1.eat()
p1.sleep()
#print(p1.eat()) #print(函数)，如果函数有返回值，则返回值会打印出来，否则打印None


print("---------------------------4、测试--------------------------------------")
'''
    self关键字：
        类中，成员属性、成员方法，使用self修饰自身的变量
'''
print("----------------01、实例化对象1-------------------")
class Person(object):
    # 获取对象属性
    def __init__(self):
        self.age = None
        self.name = None
    def get_attr(self):
        print(self.name,self.age)
p1=Person()
p1.name='ljk'
p1.age=33
p1.get_attr()#获取对象属性
print("----------------02、实例化对象2-------------------")
class Cat(object):
    # 获取对象属性
    def __init__(self,age,name): #构造方法
        self.age = age
        self.name = name
    def get_attr(self):
        print(f"{self.name}已经{self.age}岁了")
c1=Cat(10,'小花')
c1.get_attr()

print("---------------------------5、魔术方法------------------------------------")
"""
    def __魔术方法名称__():
        pass
        
    魔术方法需要考虑的几个方面：
        1、魔术方法的作用（为了解决哪些问题）:
        2、什么情况下触发魔术方法
        
    魔术方法：
        __init__()：构造方法
        __del__()：析构方法
        __str__()： 返回对象的字符串表示
        __repr__()：返回对象的字符串表示
        __len__()：返回对象的长度
        __getitem__()：返回对象中的元素
        __setitem__()：设置对象中的元素
        __delitem__()：删除对象中的元素
        __call__()：对象调用方法
        __add__()：对象相加
        __sub__()：对象相减
        __mul__()：对象相乘        
"""
print("---------------------------6、测试--------------------------------------")
print("-------------------01、魔术方法-常用使用01--------------------------")
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('构造方法调用了')
    # def __del__(self):
    #     print('析构方法调用了')
    def __str__(self):
        return f'{self.name}已经{self.age}岁了'
    # def __len__(self):
    #     return 10
    # def __getitem__(self, item):
    #     return item
    # def __setitem__(self, key, value):
    #     print(f'索引{key}，已经{value}岁了')
    # def __delitem__(self, key):
    #     print(f'索引{key}已经删除了')
    def __call__(self, *args, **kwargs): # 对象调用方法
        print(f'{self.name}已经{self.age}岁了，已经call调用了')
        return print(f"{self},call函数调用成功")
    # def __add__(self, other):
    #     return self.age+other
    # def __sub__(self, other):
    #     return self.age-other
    # def __mul__(self, other):
    #     return self.age*other
# stu1=Student('ljk',33)
# print(stu1)
# print(len(stu1))
# print(stu1[1])
# stu1[1]=10
# del stu1[1]
# stu1() # 调用对象方法
# print(stu1+1)
# print(stu1-1)
# print(stu1*2)
# del stu1 # 对象销毁,触发析构方法
# print(stu1.__str__())
# print(stu1.__len__())
# print(stu1.__getitem__(1))
# print(stu1.__setitem__(1,10))
# print(stu1.__delitem__(1))
# print(stu1.__call__())
# print(stu1.__add__(1))
# print(stu1.__sub__(1))
# print(stu1.__mul__(2))
stu=Student('ljk',33)
stu()
print("-------------------02、魔术方法-常用使用02--------------------------")





