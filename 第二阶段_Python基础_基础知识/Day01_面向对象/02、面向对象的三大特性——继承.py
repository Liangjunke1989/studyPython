# 面向对象的三大特性——继承
""""
    继承：

"""
print("---------------------------1、继承--------------------------------------")
print("--------------01、继承实例1-----------------")
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f'{self.name}可以吃')
class Dog(Animal):
    def __init__(self,name, age):
        super().__init__(name)# 调用父类的构造方法
        self.age=age
    def get_attr(self):
        print(self.name,self.age)
    def eat(self):
        super().eat() # 调用父类的方法
        print(f'{self.age}岁的{self.name}喜欢吃骨头')
    def run(self):
        print(f'{self.name}可以跑')
Dog('旺财', 10).eat() #实例化对象调用方法
print("--------------02、继承实例2-----------------")
