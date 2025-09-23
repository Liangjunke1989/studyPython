# 高级函数
"""
高级函数：
在Python中，高级函数（Higher-order Functions）是指能够接受其他函数作为参数，或者将函数作为返回值的函数。
这是函数式编程的重要特性。
"""
from functools import reduce

print("---------------------------1、内置的高级函数--------------------------------------")
# map()：map()函数接收一个函数和一个序列作为参数，将函数作用在序列的每一个元素上，并返回一个迭代器。
print("-------------01、map()--------------")
print(map(lambda x:x*x,range(1,6)))
print(list(map(lambda x:x*x,[1,2,3,4,5])))
print("-------------02、filter()--------------")
# filter()：filter()函数接收一个函数和一个序列作为参数，将函数作用在序列的每一个元素上，并返回一个迭代器。
print(filter(lambda x:x%2==0,[1,2,3,4,5]))
print(list(filter(lambda x:x%2==0,[1,2,3,4,5])))
print("-------------03、reduce()--------------")
# reduce()：reduce()函数接收一个函数和一个序列作为参数，将函数作用在序列的每一个元素上，并返回一个迭代器。
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))
'''
map/filter/reduce的区别？
    map："每个元素都转换" - 一对一映射
    filter："只保留符合条件的" - 选择性保留
    reduce："把所有元素合并成一个" - 多对一归约
'''
print("---------------------------2、自定义高级函数--------------------------------------")
print("-------------01、函数作为返回值（闭包）--------------")
def create_counter():
    """创建计数器函数"""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# 使用
counter1 = create_counter()
counter2 = create_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 - 独立的计数器

print("-------------02、函数工厂--------------")
def create_multiplier(factor):
    """创建乘法器函数"""
    def multiplier(x):
        return x * factor
    return multiplier

def create_power(exponent):
    """创建幂函数"""
    def power(base):
        return base ** exponent
    return power

# 使用
double = create_multiplier(2) #创建乘法器函数
triple = create_multiplier(3) #创建乘法器函数
square = create_power(2) #创建幂函数
cube = create_power(3) #创建幂函数

print(double(5))   # 10
print(triple(5))   # 15
print(square(4))   # 16
print(cube(3))     # 27
print("-------------03、装饰器--------------")
"""
装饰器：
装饰器（Decorator）是Python中对函数进行"包装"的语法。
"""
def my_decorator(func):
    """定义装饰器"""
    def wrapper(*args, **kwargs):
        """定义包装函数"""
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper
@my_decorator
def my_function():
    """定义被装饰的函数"""
    print("Inside my_function")

my_function()
print("-------------04、偏函数--------------")
"""
偏函数：
偏函数（Partial Function）是Python中对函数进行"部分应用"的语法。
"""
from functools import partial
def add(x, y):
    return x + y
add_five = partial(add, 5)
print(add_five(10))

