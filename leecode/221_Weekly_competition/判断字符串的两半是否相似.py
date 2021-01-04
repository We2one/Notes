#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: test
@time: 2020/12/27 16:38
@IDE: PyCharm
@desc: 判断字符串的两半是否相似
给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。

两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。

如果 a 和 b 相似，返回 true ；否则，返回 false
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # 相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）
        mid = len(s) // 2
        left, right = s[:mid].lower(), s[mid:].lower()
        count_l, count_r = 0, 0
        for i in left:
            for j in ['a', 'e', 'i', 'o','u']:
                if i == j :
                    count_l += 1
        for i in right:
            for j in ['a', 'e', 'i', 'o', 'u']:
                if i == j :
                    count_r += 1
        if count_l == count_r:
            return True
        else:
            return False


s = Solution()
print(s.halvesAreAlike('book'))