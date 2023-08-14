# -*- coding: utf-8 -*-
# @Time    : 2023/8/14 22:02
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 977_squares_of_a_sorted_array.py
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        使用新的数组存储
        时间 O(N)
        空间 O(N)
        """
        left = 0
        right = len(nums) - 1
        cur = len(nums) - 1
        result = [0] * len(nums)
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square <= right_square:
                result[cur] = right_square
                right -= 1
            else:
                result[cur] = left_square
                left += 1
            cur -= 1
        return result

