# -*- coding: utf-8 -*-
# @Time    : 2024/1/16 22:49
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 242_valid_anagram.py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        常规法
        """
        res = [0] * 26
        for i in s:
            res[ord(i)-ord('a')] += 1
        for j in t:
            res[ord(j)-ord('a')] -= 1
        return not any(res)

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        hash
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        mapping = dict()
        for i in s:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 0
        for j in t:
            if j in mapping:
                mapping[j] -= 1
            else:
                mapping[j] = 0
        for v in mapping.values():
            if v != 0:
                return False
        return True

    def isAngram3(self, s: str, t: str) -> bool:
        """使用库函数"""
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count

