# https://leetcode.com/problems/maximum-average-subarray-i/description/
class Solution:
    def findMaxAverage1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        dp = [0]
        for x in nums:
            dp.append(dp[-1] + x)
        ma = max(dp[i+k] - dp[i]  for i in range(len(nums) - k + 1))
        return ma / k
    def findMaxAverage2(self, nums, k):
        s=  sum(nums[:k])
        max_sum= s
        for i in range(len(nums)-k):
            temp= s-nums[i]+nums[i+k]
            if temp>max_sum:
                max_sum= temp
            s=temp
        return max_sum/k