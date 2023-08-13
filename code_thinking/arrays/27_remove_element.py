# -*- coding: utf-8 -*-
# @Time    : 2023/8/13 21:25
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 27_remove_element.py
#
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        暴力法
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        """

        i, l = 0, len(nums)
        while i < l:
            if nums[i] == val:  # 找到等于目标值的节点
                for j in range(i + 1, l):  # 移除该元素，并将后面元素向前平移
                    nums[j - 1] = nums[j]
                l -= 1
                i -= 1
            i += 1
        return l

    def removeElement_2(self, nums: List[int], val: int) -> int:
        """
        双指针法
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
