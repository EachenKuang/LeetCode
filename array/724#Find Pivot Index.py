# https://leetcode.com/problems/find-pivot-index/description/
class Solution:
    # 1 
    # 需要注意，pivotindex可以是头部和尾部
    # 需要考虑[-1,-1,-1,0,1,1]这种情况pivotindex为0
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
