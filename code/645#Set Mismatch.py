# https://leetcode.com/problems/set-mismatch/description/
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        once = set(nums)
        sum_whole = sum(range(len(nums)+1))  # sum of 1~n
        sum_once = sum(once)                 # sum of nums minus dupicated num
        sum_all = sum(nums)                  # sum of nums
        
        dupicated = sum_all-sum_once
        left = sum_whole -sum_once
        return [dupicated,left]
            
