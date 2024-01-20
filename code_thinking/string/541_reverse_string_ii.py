# -*- coding: utf-8 -*-
# @Time    : 2024/1/19 22:15
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 541_reverse_string_ii.py
# https://leetcode.cn/problems/reverse-string-ii/description/
from typing import List


class Solution:
    def swap(self, s: List[str], i: int, j: int):
        s[i], s[j] = s[j], s[i]

    def reverseString(self, s: List[str]) -> List[str]:
        """
        双指针
        """
        left = 0
        right = len(s) - 1
        while left < right:
            self.swap(s, left, right)
            left += 1
            right -= 1
        return s

    def reverseStr(self, s: str, k: int) -> str:
        s_list = [i for i in s]
        for i in range(0, len(s), 2*k):
            if i + k <= len(s):
                s_list[i:i+k] = self.reverseString(s_list[i:i+k])
            else:
                s_list[i:] = self.reverseString(s_list[i:])
        return "".join(s_list)

    def reverseStr2(self, s: str, k: int) -> str:
        pos = 0
        while pos < len(s):
            s = s[:pos] + s[pos:pos+k][::-1] + s[pos+k:]
            pos = pos + 2*k
        return s

    def reverseStr3(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)
