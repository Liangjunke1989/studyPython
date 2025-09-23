# 装饰器：装饰器定义一个函数，该函数是用来为其他函数添加额外的功能
# 装饰器就是不修改源代码以及调用方式的基础上增加新功能
# 开放封闭原则：
    # 开放：指的是对扩展功能是开放的
    # 封闭：指的是对修改源代码以及调用方式是封闭的
## 装饰器的语法：@decorator
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
