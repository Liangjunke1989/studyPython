# # 01、while常规练习
# none = True
# num = 0  # 常规默认值一般取值为0
# while none:
#     num += 1
#     if num < 10:
#         if num == 6:
#             # print('经历了666')
#             continue
#         print(num, end=" ")
#     else:
#         break
#         # none = False

# 02、计数器的练习
num2 = 0
while num2 < 10:
    # print('这是学习的第%d次' % (num2 + 1))
    print(f"这是学习的第{num2 + 1}次！！！")
    num2 += 1
print(f'一共计算了{num2}次')  # 局部变量和全局变量？

# 03、计数器的加强练习
i = 0
while i < 3:
    print('你叫什么？')
    j = 0
    while j < 2:
        print('我是koko')
        j += 1
    i += 1
print('完成计数器的操作')


