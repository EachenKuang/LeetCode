# https://leetcode.com/problems/rotate-array/description/
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 显然不能直接一步步移动
        # 先对K进行模运算
        if not nums:
            return
        n = len(nums)
        k = k%n
        nums[:] = nums[n-k:]+nums[:n-k]