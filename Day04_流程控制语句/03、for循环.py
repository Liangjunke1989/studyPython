# for i in range(18, 24):
#     print(i, end=' ')
# 练习：乘法表
for i in range(1, 10):
    j = i + 1
    for j in range(1, j):
        if i > j:
            if i == 6:
                continue
            print('%d * %d = %d' % (j, i, i * j), end="   ")
        elif i == j:
            print(" ")
        else:
            break
print("九九乘法表打印完成！")
