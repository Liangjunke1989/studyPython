"""
    流程结构
        1、顺序结构
            基本语法
        2、选择结构
            if 条件：
                缩进语句
        3、循环结构
"""
"""
    选择结构：4大语句 
    if语句
    if... else语句
    if...elif...else语句
    三目运算符：
        条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
"""
a = 3
b = 4
print('---------------01、一般if...else语句---------------')
if a > b:
    print('条件成立，执行1')
else:
    print('条件不成立，执行2')
print('依旧继续执行，执行3')

print('---------------02、if...elseif...else语句---------------')
if a > b:
    print('a大于b成立')
elif a == b:
    print('a等于b成立')
else:
    print('a小于b成立')

print('---------------03、三目运算符---------------')
print(a if a > b else b) # 条件成立，执行1，条件不成立，执行2
name1='ljk'
age1=36
name2='juhnko'
age2=35
print(f'名字为:%s,年龄为:%d' %(name1,age1) if a>b else f'名字为:%s,年龄为:%d' %(name2,age2))

