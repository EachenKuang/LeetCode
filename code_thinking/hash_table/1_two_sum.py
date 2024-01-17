# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 23:01
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 1_two_sum.py
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """暴力法"""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """使用字典法"""
        pair = {}
        for i in range(len(nums)):
            if nums[i] in pair.keys():
                return [pair.get(nums[i]), i]
            else:
                pair[target-nums[i]] = i
        return []


