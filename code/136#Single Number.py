class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1 使用异或
        # 只有一个数出现1次，其他都是两次，可以使用异或运算
        # a^a = 0
        # a^0 = a
        a = 0
        for i in nums:
            a ^= i
        return a
        # 2 使用加和
        # 先求出和，然后求出set,加和后乘2减去SUM
     def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return(sum(set(nums))*2 - sum(nums))