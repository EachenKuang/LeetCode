# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
class Solution:
    # 1
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        n = len(nums)
        cmax, cmin = -float('inf'), float('inf')
        l, r = 0, -1
        for i in range(n):
            cmax = max(cmax, nums[i])
            cmin = min(cmin, nums[n - 1 - i])
            if nums[i] != cmax: r = i
            if nums[n - 1 - i] != cmin: l = n - 1 - i
        return r - l + 1
    # 
    #  thank @lee215
    # 比较与排序好的数组，使用zip然比较 
    def findUnsortedSubarray(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)