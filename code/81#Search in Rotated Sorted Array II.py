# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return True
            if target < nums[mid]:
                if nums[left] < nums[right]:
                    right = mid - 1
                else:
                    if target == nums[left]:
                        return True
                    if target < nums[left]:
                        left += 1
                    else:
                        right = mid - 1
            else:
                if nums[left] < nums[right]:
                    left = mid + 1
                else:
                    if target == nums[left]:
                        return True
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        left += 1
        if nums[left] == target:
            return True
        return True if nums[right] == target else False

    def search(self, nums, target):
        return target in nums
