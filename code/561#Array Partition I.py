# https://leetcode.com/problems/array-partition-i/description/
class Solution(object):
	# 事实上只要知道这个最大的逻辑
	# 对于（1，2，3，4），（1，2）（3，4）组合最大
	# 所以思路是：先按照顺序排序，然后两两组合。
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums[::2]))