# https://leetcode.com/problems/move-zeroes/description/
class Solution:
    # 1 最快想出来的方法
    # 使用remove和append
    # 10.98% 速度还是较慢
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
    # 2 O(n)
    # 99.97%
    # 只管非零的数，后面直接补齐0
    def moveZeroes(self, nums):
        left = 0
        for num in nums:
            if num != 0:
                nums[left] = num
                left += 1
        while left < len(nums):
            nums[left] = 0
            left += 1
                