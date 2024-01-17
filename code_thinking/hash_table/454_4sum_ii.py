# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 23:07
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 454_4sum_ii.py
# https://leetcode.cn/problems/4sum-ii/
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        常规思路：
        1. 将4个数组分成两组
        2. 对前组全连接后先计算出和，得到一个字典，key 为两数之和，value 为这种组合的个数
        3. 对后两组，两个for循环之后，计算 两数之和的相反数是否在 上述得到的字典中，然后计数器加上 value的值
        4. 最终得到的数就是结果
        时间:  O(n^2)
        空间:  O(n^2) 最大情况为 两个数组的所有数都不相等，导致需要存储 N*N 个键值对
        """
        res = dict()
        for i in nums1:
            for j in nums2:
                if i + j in res:
                    res[i+j] += 1
                else:
                    res[i+j] = 1
        count = 0
        for i in nums3:
            for j in nums4:
                if - i - j in res:
                    count += res[-i-j]
        return count
