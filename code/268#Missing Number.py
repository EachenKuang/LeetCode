# https://leetcode.com/problems/missing-number/description/
class Solution:
    # 1 常规：O(n2) time out 失败
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        for i in range(len(nums)+1):
            if i not in nums:
                return i
    
    # 2 
    # 1中变式，使用set判断是否包含O(n) 
    # 83.90%
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        s = set(nums)
        for i in range(len(nums)+1):
            if i not in s:
                return i
    # 3
    # O(n) 99.58%
    # 使用和的方法求出缺少的数
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        n = len(nums)
        return n*(n+1)//2-sum(nums)