#  计算0～100之间所有偶数的累积求和结果
# 编写循环 确认要记算的数字
# 添加结果变量，在循环内部处理计算结果
result = 0
i = 0
while i<= 100:
    # 判断变量 i 中的数值，是否是一个偶数
    # i% 2 == 0
    if i % 2 == 0:
        print(i)
        result += i
    i += 1
print("偶数求和结果是 %d "% result)


