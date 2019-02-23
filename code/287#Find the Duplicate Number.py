# https://leetcode.com/problems/find-the-duplicate-number/
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution:
    # 1
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            else:
                num_set.add(num)

    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = temp = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        while True:
            slow = nums[slow]
            temp = nums[temp]
            if slow == temp:
                break
        return slow