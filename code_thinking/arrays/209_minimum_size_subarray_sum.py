# -*- coding: utf-8 -*-
# @Time    : 2023/8/14 22:24
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 209_minimum_size_subarray_sum.py
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
# 示例：
#
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 提示：
#
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# #算法公开课
# https://leetcode.cn/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        暴力破解法
        两个for循环 i表示开始位置，j表示结束位置
        """
        min_len = float('inf')
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                if cur_sum >= target:
                    min_len = min(min_len, j - i + 1)
                    break
        return min_len if min_len != float('inf') else 0

    def minSubArrayLen_2(self, target: int, nums: List[int]) -> int:
        """
        双指针法
        """
        i = 0
        cur_sum = 0
        min_len = float('inf')

        for j in range(len(nums)):
            cur_sum += nums[j]
            while cur_sum >= target:
                min_len = min(min_len, j - i + 1)
                cur_sum -= nums[i]
                i += 1
        return min_len if min_len != float('inf') else 0

