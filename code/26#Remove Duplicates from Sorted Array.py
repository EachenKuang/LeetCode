# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)