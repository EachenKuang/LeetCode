# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
# 常规法 O(n)
# 36ms
class Solution1:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
# 二分法
# 36ms
class Solution2:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
        	mid = left + (right - left)//2
        	if nums[mid] <= nums[mid-1]:
        		return nums[mid]
        	else:
        		if nums[mid] > nums[right]:
        			left = mid + 1
        		else:
        			right = mid - 1
        return None

