# https://leetcode.com/problems/contiguous-array/
"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        track,has=0,{0:-1}
        length=len(nums);
        ress_max=0;
        
        for i in range(0,length):
            track += (1 if nums[i]==1 else -1)
            if  track not in has:
                has[track]=i
            elif ress_max <i-has[track]:
                ress_max = i-has[track]
        return ress_max
        
