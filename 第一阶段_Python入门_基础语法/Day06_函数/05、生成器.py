"""
    生成器（Generator）
        基本概念:
            本质是一种特殊的迭代器，使用 yield 关键字实现
            函数执行到 yield 时暂停并返回值，下次调用从暂停处继续执行
            更简洁地创建迭代器
        创建方式:
            生成器函数：包含 yield 的函数
            生成器表达式：类似列表推导式的语法
        解决了内存优化问题
"""
# 生成器函数
def my_generator():
    print("生成器函数开始执行")
    yield 1
    print("生成器函数暂停执行")
    yield 2
    print("生成器函数继续执行")
    yield 3
    print("生成器函数结束执行")
g=my_generator()
print(g.__iter__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__iter__())

# 生成器表达式
gen = (x*x for x in range(5))
for i in gen:
    print(i)



