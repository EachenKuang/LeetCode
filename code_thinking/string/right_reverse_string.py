# -*- coding: utf-8 -*-
# @Time    : 2024/1/20 15:58
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : right_reverse_string.py
# https://www.programmercarl.com/kama55.%E5%8F%B3%E6%97%8B%E5%AD%97%E7%AC%A6%E4%B8%B2.html#%E6%80%9D%E8%B7%AF
# 字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。
#
# 例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。
#
# 输入：输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。
#
# 输出：输出共一行，为进行了右旋转操作后的字符串。
from typing import List


class Solution:
    def right_reverse_string(self, s: str, k: int):
        """一行代码
        利用特性，不推荐
        """
        return s[-k:] + s[:-k]

    def swap(self, s: List[str], i: int, j: int):
        s[i], s[j] = s[j], s[i]

    def right_reverse_string2(self, s: str, k: int):
        """
        两极反转，先整体进行翻转，然后对前K个进行翻转，后面的进行翻转
        k = 2
        a b  c d e f g
        g f  e d c b a
        f g  a b c d e
        """
        length = len(s)
        if k >= length:
            # k 的长度大于整体的长度，不需要翻转
            return s
        # 整体进行翻转
        left = 0
        right = length - 1
        s_list = list(s)  # python 中的字符串是不可变的，所以需要使用列表来处理
        self.reverse_between(left, right, s_list)
        self.reverse_between(0, k-1, s_list)
        self.reverse_between(k, length-1, s_list)

        return "".join(s_list)

    def reverse_between(self, left, right, s_list: List[str]):
        while left < right:
            self.swap(s_list, left, right)
            left += 1
            right -= 1
    # 对 [0,k) 进行翻转 [k,length) 进行翻转


if __name__ == '__main__':
    solution = Solution()
    print(solution.right_reverse_string("abcdefg", 100))

    print(solution.right_reverse_string2("abcdefg", 1))

