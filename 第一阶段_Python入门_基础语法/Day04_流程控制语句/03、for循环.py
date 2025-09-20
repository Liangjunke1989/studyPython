# range()的范围：[start, end)
for i in range(5):
    print(i, end='，')
print('\n')
print('--------------------')
for i in range(18, 24):
    print(i, end='，')
print('\n')
print('--------------------')
# 练习：乘法表
# for i in range(1, 10):
#     j = i + 1
#     for j in range(1, j):
#         if i > j:
#             # if i == 6:
#             #     continue
#             print('%d * %d = %d' % (j, i, i * j), end="   ")
#         elif i == j:
#             print('%d * %d = %d' % (i, j, i * j), end="\t \n ")
#         else:
#             break
# print("九九乘法表打印完成！")

# 重新写一个'九九乘法表'，需要开头对齐
for i in range(1, 10):
    for j in range(1, i + 1):
        if i==5:
            continue # 跳过第5行
        print('%d * %d = %d' % (j, i, i * j), end="   ")
        if i == j:
            print('\n')
            break   #
print("九九乘法表打印完成！")

