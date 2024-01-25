# -*- coding: utf-8 -*-
# @Time    : 2024/1/21 17:21
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 459_repeated_substring_pattern.py
# https://leetcode.cn/problems/repeated-substring-pattern/submissions/497218492/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """如果符合要求"""
        new_str = s + s
        return s in new_str[1:-1]

    def repeatedSubstringPattern2(self, s: str) -> bool:
        """使用find"""
        s1 = s + s
        return s1[1:len(s1) - 1].find(s) >= 0

    def repeatedSubstringPattern3(self, s: str) -> bool:
        pass
