# https://leetcode.com/problems/non-decreasing-array/description/
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i
        return (p is None or p == 0 or p == len(nums)-2 or 
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
    


