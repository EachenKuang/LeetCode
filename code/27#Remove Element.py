# https://leetcode.com/problems/remove-element/description/
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        times = nums.count(val)
        while times>0:
            nums.remove(val)
            times-=1
        return len(nums)