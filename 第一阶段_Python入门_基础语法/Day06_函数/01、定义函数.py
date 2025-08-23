"""
    函数的说明文档的使用：
    # help(display):查看函数的说明文档（函数的解释说明信息）
"""


def display01(a):
    """说明文档位置"""
    return print('显示"我是新定义的函数"')

print("__________________________________")


def display02(b):
    """
    函数说明文档展示
    :param b 字符串参数
    :return 打印输出参数
    """
    return print('我是函数定义案例展示！')

display01(print('密码正确登录成功'))
help(display01)
help(display02)
