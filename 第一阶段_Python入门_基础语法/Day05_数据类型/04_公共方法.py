# 公共方法
from traceback import print_tb

print("------------------1、模块级函数--------------------")
def display01(a):
    print('显示"我是新定义的函数"')
    print(a)
display01("我是参数")

print('------------------2、类中的公共方法--------------------')
class MyClass:
    # 实例方法
    def public_method(self, param):
        return f"公共方法: {param}"
    # 类方法
    @classmethod
    def class_method(cls, param):
        return f"类方法: {param}"
    # 静态方法
    @staticmethod
    def static_method(param):
        return f"静态方法: {param}"
class1=MyClass()
print(class1.public_method("实例调用"))
print(MyClass.class_method("类调用"))
print(MyClass.static_method("静态调用"))