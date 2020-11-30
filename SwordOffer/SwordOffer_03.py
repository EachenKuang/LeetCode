# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
# 找出数组中重复的数字。
#
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 示例 1：
#
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
#
# 限制：
# 2 <= n <= 100000
from typing import List


class Solution:

    def findRepeatNumber(self, nums: List[int]) -> int:
        """
        第一种方法
        维持一个数组，a[n] 位置保存对应的数的个数
        空间上有些浪费
        """
        length = len(nums)
        store = [0] * length
        for num in nums:
            store[num] += 1
            if store[num] >= 2:
                return num
        return -1

    def findRepeatNumber2(self, nums: List[int]) -> int:
        """
        第二种方法
        把方法一中的数组换成字典来存储，不需要初始化空间，查找也是O(1)
        """
        find_dict = dict()
        for num in nums:
            if num in find_dict:
                return num
            else:
                find_dict[num] = 0

    def findRepeatNumber2_2(self, nums: List[int]) -> int:
        """
        第二种的改版
        字典用set来存储
        """
        find_set = set()
        for num in nums:
            if num in find_set:
                return num
            else:
                find_set.add(num)


if __name__ == '__main__':
    solution = Solution()
    input_items = [2, 3, 1, 0, 2, 5, 3]
    output_items1 = solution.findRepeatNumber(input_items)
    assert output_items1 == 2
    output_items2 = solution.findRepeatNumber2(input_items)
    assert output_items2 == 2
    output_items2_2 = solution.findRepeatNumber2_2(input_items)
    assert output_items2_2 == 2
