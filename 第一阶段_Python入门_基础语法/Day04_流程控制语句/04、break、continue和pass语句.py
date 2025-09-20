"""
    break:终止当前循环
    continue:中止本次循环，进入下一次循环
    pass:占位，空语句
"""
"""
break 和 continue的区别？

    break
    作用：立即终止整个循环，跳出循环体
    使用场景：当满足某个条件时，完全结束循环
    影响范围：直接退出当前循环，不再执行循环中剩余的任何代码
    
    continue
    作用：跳过当前循环迭代的剩余代码，直接进入下一次循环
    使用场景：当满足某个条件时，跳过本次循环的剩余部分
    影响范围：只跳过当前这一次循环，循环会继续执行
    
    执行结果：
    break：完全结束循环
    continue：只跳过当前迭代，循环继续
    流程控制：
    break：跳出循环体
    continue：跳到循环的下一个迭代
    使用目的：
    break：用于提前终止循环
    continue：用于跳过特定条件下的处理

"""
print('-------------------break--------------')
for i in range(10):
    if i == 5:
        break  # 当i等于5时，直接跳出循环
    print(i)
# 输出: 0 1 2 3 4
print('-------------------continue--------------')
for i in range(10):
    if i==5:
        continue  # 跳过偶数，不执行print语句
    print(i)
print('-------------------pass--------------')
for i in range(10):
    if i==5:
        pass  # 占位，空语句，后期再添加逻辑
        print('11')
    #print(i)

