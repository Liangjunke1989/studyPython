print("------------------------string字符串---------------------------")
print("------------------1、字符串入门--------------------")
# 字符串不允许之间或其他类型的数据拼接。
str1 = "我是山东人"
num1 = 12345
str2 = "I am LJK"
print(str1 + str(num1) + str2)

print("------------计算字符串的长度--------------")
str3 = "人生苦短，我用Python!"
print(len(str3))  # 14
print(len(str3.encode()))  # 28
print(len(str3.encode('gbk')))  # 21

print("------------截取字符串-------------------")
# string[start:end:step]  包含开始不包含结束，步长默认为1
substr1 = str3[2:8]
print(substr1)
substr2 = str3[2:8:2]
print(substr2)

print("------------分割、合并字符串--------------")
'''
    分割字符串
    str.split(sep,maxsplit) 
    sep:用于指定分隔符，可以包含多个字符。
        默认为None，即所有空字符（包括空格、换行"\n"、制表符"\t"）
    maxsplit:可选参数，用于指定分割的次数，不指定为没有限制，
            否则返回结果列表的元素个数最多为maxsplit+1。
'''
str4 = "明 日 学 院 官 网      》》》 www.ljk3d.com"
print(str4.split())
print(str4.split("》》》"))
'''
    合并字符串
    strnew=string.join(iterable)
    string:字符串类型，用于指定合并时的分隔符。
    strnew:表示合并后生成的新字符串。
        默认为None，即所有空字符（包括空格、换行"\n"、制表符"\t"）
    iterable:可迭代对象，该迭代对象中的所有元素（字符串表示）将被合并为一个新的字符串
'''
string66 = "@"
list_friend = ['ljk', 'koko', 'juhnko']
print('@' + string66.join(list_friend))
print("------------字符串字母的大小写转换--------------")
'''
    lower():
    uppper():
'''
str5 = "abcdefGHIJKLMN"
print(str5.lower())
print(str5.upper())
print("------------去除字符串中的空格和特殊字符--------------")
'''
    strip(): 去掉字符串左、右两侧的空格和特殊字符。
    str.lstrip(): 去掉字符串左侧的空格和特殊字符。
    str.rstrip(): 去掉字符串右侧的空格和特殊字符。
'''
str6='http://www.ljk3d.com \t\n\r'
print(str6)
print(str6.strip('http://'))
print()
print("------------------2、字符串常见操作--------------------")
print("------------格式化字符串--------------")
'''
   使用"%"操作符
    
   使用字符串对象的format()方法
    
'''
print("------------字符串的增删改查--------------")
'''
    查:
        下标: 计算机为数据序列每个元素分配的从0开始的编号
        count(): 统计某个数据在列表中出现的次数。
        find():  如果不存在，返回-1
        index(): 如果不存在，报错
        startswith()
        endswith()
'''

print()
print("------------------3、字符串延展操作--------------------")
print("------------字符串的对齐--------------")
'''
    左对齐: str.ljust(10)
    右对齐: str.rjust(10)
    中间对齐: str.center(10)
'''
str111 = "hello"
print(str111.ljust(10, '.'))
