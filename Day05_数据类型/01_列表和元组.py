list1 = ['koko', 123, 'ljk', 0.56]
# # 1.index()
# print(list1.index('ljk', 1, 3))
#
# # 2. count()和len()
# print(list1.count(123))  # 某个元素的出现的个数
# print(len(list1))
#
# # 3.in
# print(123 in list1)
# print(13 not in list1)

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
# 7.list的"查": 列表的循环遍历
list5 = ['tom', 'jerry', 'rose', 'jike']
print("-----------while遍历-----------")
# # while实现遍历
i = 0
while i < len(list5):
    print(list5[i], end=" ")
    i += 1
# for循环实现遍历
print("-----------for...in...遍历-----------")
for j in list5:
    print(j, end=" ")
