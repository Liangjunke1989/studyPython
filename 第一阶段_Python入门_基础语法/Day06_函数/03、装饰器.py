"""
 装饰器：
   装饰器是一种设计模式，它允许在不修改源代码的情况下，为函数添加新的功能。
   装饰器定义一个函数，该函数是用来为其他函数添加额外的功能
   本质是一个接受函数作为参数并返回函数的高阶函数
   装饰器的语法：@decorator

   解决了功能增强的问题
"""
# 开放封闭原则：
    # 开放：指的是对扩展功能是开放的
    # 封闭：指的是对修改源代码以及调用方式是封闭的
def decorator(func):
    def wrapper(*args, **kwargs):
        print("开始执行")
        func(*args, **kwargs)
        print("结束执行")
        return func(*args, **kwargs)
    return wrapper
@decorator
def display01(a):
    """说明文档位置"""
    return 1
print(display01(1))
