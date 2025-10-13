"""
    迭代器：
        基本概念：
            实现了迭代协议的对象，可以被 for 循环遍历
            必须实现 __iter__() 和 __next__() 方法
            __iter__()：返回迭代器对象本身
            __next__()：返回下一个元素，没有元素时抛出 StopIteration 异常
            支持惰性计算，节省内存
        解决了数据遍历的问题
"""
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

