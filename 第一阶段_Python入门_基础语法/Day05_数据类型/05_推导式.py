# 推导式：
"""
1. 基本概念
    推导式（Comprehension）是Python提供的一种简洁、优雅的方式
    来创建列表、字典、集合和生成器表达式。
    它可以在一行代码中完成循环和条件判断，使代码更加简洁易读。
"""
# 语法：
# [expression for item in iterable]
# [expression for item in iterable if condition]
# {key_expression: value_expression for item in iterable}
# {expression for item in iterable}
# (expression for item in iterable)

print("------------------1、列表推导式--------------------")
# 基本用法
squares = [x**2 for x in range(10)]
print("------------------2、带条件的列表推导式--------------------")
# 带条件
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("------------------3、嵌套推导式--------------------")
# 嵌套循环
matrix = [[i*j for j in range(3)] for i in range(3)]
print("------------------4、字典推导式--------------------")
# 创建字典
squares_dict = {x: x**2 for x in range(5)}
print("------------------5、带条件的字典推导式--------------------")
# 带条件
even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print("------------------6、集合推导式--------------------")
# 创建集合
unique_squares = {x**2 for x in range(-5, 6)}
# 去重
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = {x for x in numbers}
print("------------------7、生成器推导式--------------------")
# 创建生成器
squares_gen = (x**2 for x in range(10))
# 使用生成器
for square in squares_gen:
    print(square)
print("------------------8、嵌套推导式--------------------")
# 嵌套列表推导式
matrix = [[i*j for j in range(3)] for i in range(3)]
# 扁平化嵌套列表
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]


