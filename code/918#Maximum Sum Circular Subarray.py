# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""
'''
53.Maximum Subarray 
# https://leetcode.com/problems/maximum-subarray/description/
这道题的关键是怎样解决圈的问题
对于53题
    # class Solution:
    #     def maxSubArray(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: int
    #         策略：遍历所有数，如果当前和小于0，则从下一个数开始重新算
    #         用res保存当前最大，current_sum保存遍历数组的和大小
    #         """
    #         res = nums[0] 
    #         current_sum = nums[0]
    #         for i in range(1,len(nums)):
    #             current_sum = max(current_sum + nums[i], nums[i])
    #             res = max(res, current_sum)
    #         return res
此题可以分为两种情况：
1：最大子序列不过端点，等同于53题的情况
2：最大子序列需要过端点，等同于在序列中先找到最小子序列，然后用总和减去最小子序列

max(the max subarray sum, the total sum - the min subarray sum)
'''

def maxSubarraySumCircular(self, A):
    total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
    for a in A:
        curMax = max(curMax + a, a)
        maxSum = max(maxSum, curMax)
        curMin = min(curMin + a, a)
        minSum = min(minSum, curMin)
        total += a
    return max(maxSum, total - minSum) if maxSum > 0 else maxSum