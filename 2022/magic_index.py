from typing import List
# 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，
# 若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
#
# 示例1:
#
#  输入：nums = [0, 2, 3, 4, 5]
#  输出：0
#  说明: 0下标的元素为0
# 示例2:
#
#  输入：nums = [1, 1, 1]
#  输出：1
# 说明:
#
# nums长度在[1, 1000000]之间
# 此题为原书中的 Follow-up，即数组中可能包含重复元素的版本


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        """
        直接遍历全数据
        时间复杂度 O(N)
        """
        for i, v in enumerate(nums):
            if i == v:
                return i
        return -1

    def findMagicIndex1(self, nums: List[int]) -> int:
        """
        因为是有序数组，可以使用二分法
        时间复杂度可以达到 O(lnN)
        """
        length = len(nums)
        left = 0
        right = length - 1
        while left <= right:
            # 因为长度在 1, 1000000 之间，可以直接相加，如果两和超过int，就需要使用
            # left + (right - left) // 2
            mid = (right + left) // 2
            if mid >= nums[mid]:
                pass
            else:
                pass




if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [1, 1, 3, 4],
        [1, 1, 1]
    ]
    results = [
        1,
        1
    ]
    for i in range(len(test_cases)):
        assert solution.findMagicIndex(test_cases[i]) == results[i]

