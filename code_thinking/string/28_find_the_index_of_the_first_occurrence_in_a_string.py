# -*- coding: utf-8 -*-
# @Time    : 2024/1/21 16:49
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 28_find_the_index_of_the_first_occurrence_in_a_string.py
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    # KMP算法
    def getNext(self, next, s):
        """前缀表"""
        j = -1
        next[0] = j
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j + 1]:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j

    def strStr3(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j + 1]:
                j = next[j]
            if haystack[i] == needle[j + 1]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1


if __name__ == '__main__':
    haystack = "soadbutsad"
    needle = "sad"
    solution = Solution()
    print(solution.strStr3(haystack, needle))