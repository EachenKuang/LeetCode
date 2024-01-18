# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 23:24
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 18_4sum.py
# https://leetcode.cn/problems/4sum/description/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        时间复杂度 O(n^3)
        """
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            # 剪枝
            if nums[i] > target and nums[i] > 0:
                break
            # 对 i 进行去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, length):
                # 剪枝
                if nums[i] + nums[j] > target and nums[i] + nums[j] > 0:
                    break
                # 对 j 进行去重
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = length - 1
                while left < right:
                    sum_of_four = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_of_four > target:
                        right -= 1
                    elif sum_of_four < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # 去重，特别注意，这里需要在插入数据之后才能进行去重，例如 0，0，0，0 的情况
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res
