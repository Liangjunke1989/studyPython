print("----------------1、列表-------------------------")
'''
    序列：
        序列是一块用于存储多个值的连续内存空间。
        序列结构有：列表、元组、字典、集合、字符串。
    应用场景：
        列表一次性可以存储多个数据，且可以为不同数据类型。
    列表的特点：
        列表是可变序列。
    列表的常见操作：    
    “增”
        append():追加列表的话，将追加整个列表作为最后一个数据结尾，最后一个数据为列表
        extend():追加列表结尾，将数据序列拆开，逐一追加
    “删”
        del: 可以删除指定下标的数据
        pop(): 删除指定下标的数据，如果不指定下标，默认删除最后一个数据。
               无论是按照下标还是默认，pop()函数都会返回这个被删除的数据
        remove(): 移除列表中的某个数据的第一个匹配项。
        clear():  清空列表
    “改”
        reverse() 逆置
        sort()  排序
    “查”
        index(): 查找某个数据，如果数据存在返回对应的下标，否则报错
        count(): 统计某个数据在列表中出现的次数。
        len(): 统计列表中数据的个数。
        in: 判断某个元素是否在列表中。
        list列表的循环遍历:
            while
            for...in...
    列表的推导式:
        list=[Expression for var in range]
        newlist=[Expression for var in list]
'''
print("----------------1.1、列表入门-------------------------")
list1 = ['koko', 123, 'ljk', 0.56]
# 1.index()
print(list1.index('ljk', 1, 3))
# 2. count()和len()
print(list1.count(123))  # 某个元素的出现的个数
print(len(list1))
# 3.in
print(123 in list1)
print(13 not in list1)
print("----------------1.2、列表的常见操作-------------------------")
print("----------------1.2.1、列表的增-------------------------")
# 4.list的"增":  append()、extend()和insert()
list1.append("小明")
print(list1)
list2 = ['阿强', '阿虎']
list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)
list1.insert(5, 'dk')  # 下标为5的地方添加
print(list1)
print("----------------1.2.2、列表的删-------------------------")
# 5.list的"删":  del()、pop()、remove()和clear()
# del list1
del list2[1]
print(list2)
# pop()
name1 = list1.pop(5)
print(name1)
print(list1)
# remove()
list1.remove("小明")
print(list1)
# clear()
# list1.clear()
print(list1)
print("----------------1.2.3、列表的改-------------------------")
# 6.list的"改": del()、pop()、remove()和clear()
list1[2] = "小明"
print(list1)
#  逆序
list3 = [1, 2, 3, 43, 5, 26, 7]
list3.reverse()
print(list3)
#  升序和降序
list4 = [12, 1, 4, 5, 2, 3]
list4.sort()  # 默认生序
print(list4)
list4.sort(reverse=True)
print(list4)
print("----------------1.2.4、列表的查-------------------------")
# 7.list的"查": 列表的循环遍历
list5 = ['tom', 'jerry', 'rose', 'jike']
print("-----------while遍历-----------")
# # while实现遍历
i = 0
while i < len(list5):
    print(list5[i], end=" ")
    i += 1
print()
# for循环实现遍历
print("-----------for...in...遍历-----------")
for j in list5:
    print(j, end=" ")
print()
print("----------------1.3、列表的嵌套-------------------------")
# 8.列表的嵌套使用：类似于多维数组
name_list = [['tom', 'lily', 'juhnko'], ['张三', '李四', '王五'], [123, 456, 789]]
print(name_list[1][2])
print()

print("--------------------------2、元组------------------------------")
'''
    应用场景：
        一个元组可以存储多个数据，元组内的元素是不能修改的。
    元组的特点：
        定义元组使用小括号，且逗号隔开各个数据，数据可以是不同的数据类型。
        元组是不可变序列。
    元组的定义：
        # 多个数据元组
        # 单个数据元组
    元组的推导式：
        
'''
# 1.定义多个数据元组
t1 = (10, 20, 30, 40, 50)
print(t1)
print(type(t1))
# 2.定义当个数据元组
t2 = (10,)
print(t2)
print(type(t2))
t3 = (10)  # 单个元素是int类型，原先数据是什么类型，输出的就是什么类型。
print(t3)
print(type(t3))
print("--------------------------2.1、元组的常见操作------------------------------")
'''
    元组数据不支持修改，只支持查找。
    查：
        按下标查找数据: 返回对应的值。
        index(): 查找某个数据，如果数据存在返回对应的下标，否则报错，语法与列表、字符串的index方法相同。
        count(): 统计某个数据在列表中出现的次数。
        len(): 统计元组中数据的个数。
'''
# 1.下标
print(t1[0])
# 2.index()
print(t1.index(10, 0, 2))
# 3.count()
print(t1.count(10))
# 4.len()
print(len(t1))  # 5
print("--------------------------2.2、元组中列表是可以修改的------------------------------")
t4 = ('1', [1, 2, 3], 123)
print(t4)
t4[1][1] = 8
print(t4)
