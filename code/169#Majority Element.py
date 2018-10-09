# https://leetcode.com/problems/majority-element/description/
class Solution:
    # 1 如果某个数大于n/2，那么排序后的数列中，该数一定位于中位数
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]
    # 2 数数法 不推荐
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        l = len(nums)
        num = set(nums)
        for val in num:
            a = nums.count(val)
            if a >= l*0.5:
                return val
                