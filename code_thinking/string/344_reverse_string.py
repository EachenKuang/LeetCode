# -*- coding: utf-8 -*-
# @Time    : 2024/1/19 22:01
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 344_reverse_string.py
# https://leetcode.cn/problems/reverse-string/
from typing import List


class Solution:
    def swap(self, s: List[str], i: int, j: int):
        s[i], s[j] = s[j], s[i]

    def swap2(self, s: List[str], i: int, j: int):
        temp = s[i]
        s[j] = s[i]
        s[i] = temp

    def swap3(self, s: List[str], i: int, j: int):
        s[i] ^= s[j]
        s[j] ^= s[i]
        s[i] ^= s[j]

    def reverseString(self, s: List[str]) -> None:
        """
        for 循环
        """
        length = len(s)
        for i in range(length // 2):
            self.swap(s, i, length - i - 1)

    def reverseString2(self, s: List[str]) -> None:
        """
        双指针
        """
        left = 0
        right = len(s) - 1
        while left < right:
            self.swap(s, left, right)
            left += 1
            right -= 1
