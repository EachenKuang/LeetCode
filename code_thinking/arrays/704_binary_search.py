# -*- coding: utf-8 -*-
# @Time    : 2023/8/13 20:58
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 704_binary_search.py
# https://leetcode.cn/problems/binary-search/
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
# 提示：
#
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。
from typing import List


class Solution:
    """
    使用二分法，需要同时满足两个体条件：
    1、有顺序
    2、无重复
    """
    def search(self, nums: List[int], target: int) -> int:
        """
        时间复杂度：O(log n)
        空间复杂度：O(1)
        [左闭右闭区间]
        """
        left, right = 0, len(nums) - 1  # 左闭右闭区间，while条件使用<=
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def search_2(self, nums: List[int], target: int) -> int:
        """
        时间复杂度：O(log n)
        空间复杂度：O(1)
        [左闭右开区间）
        """
        left, right = 0, len(nums)  # 左闭右开区间，while条件使用<
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [-4, 5, 6, 10, 999]
    target = 19
    assert -1 == solution.search(nums, target)
    assert -1 == solution.search_2(nums, target)
