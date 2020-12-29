#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: 吃苹果的最大数目
@time: 2020/12/27 16:46
@IDE: PyCharm
@desc: 吃苹果的最大数目
有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，
这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。
你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。
给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。
"""

# apples = [1, 2, 3, 5, 2]
# days = [3, 2, 1, 4, 2]
# apples = [3,0,0,0,0,2 ]
# days = [3,0,0,0,0,2]
apples = [3,1,1,0,0,2]
days = [3,1,1,0,0,2]
bad_day = [days[i]+i for i in range(len(days))]
print(bad_day)
day_min, day_max = bad_day[0], bad_day[-1]
arr = []
for j in range(len(bad_day)):
    if j == 0 or j == len(bad_day)-1:
        apple = 0
        for i, v in enumerate(apples):
            if bad_day[j] < i+1:
                break
            apple += v
        arr.append(apple)
print(arr)
if max(arr) < len(apples):
    print(max(arr))
else:
    print(max(arr)-min(arr))

