# https://leetcode.com/problems/range-sum-query-immutable/description/

# 1 简洁版
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# 2 高效版 beat 99%
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.presum = None
        if nums:
            self.presum = [0] * (1+len(nums))
            for i in range(1, 1+len(nums), 1):
                self.presum[i] = nums[i-1] + self.presum[i-1]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.presum[j+1] - self.presum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)