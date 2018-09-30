# https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0        
        if target<nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low + (high-low)//target
            if  target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high =mid-1
        return low