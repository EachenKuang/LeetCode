# https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        策略：遍历所有数，如果当前和小于0，则从下一个数开始重新算
        用res保存当前最大，current_sum保存遍历数组的和大小
        """
        res = nums[0] 
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            res = max(res, current_sum)
        return res