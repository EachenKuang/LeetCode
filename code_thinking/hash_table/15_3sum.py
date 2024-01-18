# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 22:18
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 15_3sum.py
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1.先排序
        2.固定第一位i，然后使用双指针找寻j,k
        3. 如果 nums[i] + nums[j] + nums[k] > 0:
            k--
            如果 nums[i] + nums[j] + nums[k] < 0:
            i++
            如果 nums[i] + nums[j] + nums[k] = 0:
            收获结果道数组中
        """
        res = []
        nums.sort()
        length = len(nums)
        for i in range(0, length):
            # 第一层剪枝
            if nums[i] > 0:
                break
            # 第一层去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                sum_of_three = nums[i] + nums[left] + nums[right]
                if sum_of_three > 0:
                    right -= 1
                elif sum_of_three < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # 去重，特别注意，这里需要在插入数据之后才能进行去重，例如 0，0，0，0 的情况
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
