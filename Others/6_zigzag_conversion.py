# -*- coding: utf-8 -*-
# @Time    : 2024/1/25 22:22
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 6_zigzag_conversion.py
# https://leetcode.cn/problems/zigzag-conversion/description/
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """第一版"""
        if numRows == 1 or numRows >= len(s):
            # 剪枝
            return s
        matrix = [[] for _ in range(numRows)]  # 构造一个 numRows 的 list
        index = 0
        desc = True
        for i in s:
            matrix[index].append(i)
            # 不同情况
            if desc:
                # 正向执行
                index += 1
                if index == numRows - 1:
                    # 到了边界，需要转向
                    desc = False
            else:
                # 逆向执行
                index -= 1
                if index == 0:
                    # 到了边界
                    desc = True
        result = ""
        for m in matrix:
            result += "".join(m)
        return result

    def convert2(self, s: str, numRows: int) -> str:
        """第二版，优化下循环中"""
        if numRows == 1 or numRows >= len(s):
            return s
        matrix = [[] for _ in range(numRows)]  # 构造一个 numRows 的 list
        index = 0
        flag = -1
        for i in s:
            matrix[index].append(i)
            if index == 0 or index == numRows-1:
                # 边界上需要调整方向
                flag = -flag
            index += flag
        result = ""
        for m in matrix:
            result += "".join(m)
        return result

import random