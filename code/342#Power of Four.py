# https://leetcode.com/problems/power-of-four/description/
class Solution:
    # 1 常规方法
    # n小于等于0 FALSE
    # n等于1  TRUE
    # n大于1  需要判断
    def isPowerOfFour(self, num):
        """
        :type n: int
        :rtype: bool
        """
        if num<=0:
            return False
        while num>1:
            if num%4==0:
                num//=4
            else:
                return False
        return True
    # 2 技巧
    # 4的倍数 二进制位 0100 与 0011 且操作 为0，
    def isPowerOfFour(self, num):
        """
        :type n: int
        :rtype: bool
        """
        return (num > 0) and (num & (num-1) == 0) and (num & 0xAAAAAAAA) == 0 
    # 3 递归 常规方法变式
    def isPowerOfFour(self, num):
        """
        :type n: int
        :rtype: bool
        """
        return num>0 and (num==1 or (num%4==0 and self.isPowerOfFour(num/4)))