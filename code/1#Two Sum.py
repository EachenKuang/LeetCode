# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair = {}
        for i in range(len(nums)):
            if nums[i] in pair.keys():
                return [pair.get(nums[i]),i]
            else:
                pair[target-nums[i]] = i
        return []
