# https://leetcode.com/problems/power-of-three/description/
class Solution:
    # 1 常规方法
    # n小于等于0 FALSE
    # n等于1  TRUE
    # n大于1  需要判断
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n>1:
            if n%3==0:
                n//=3
            else:
                return False
        return True
    # 2 技巧
    # M=1162261467=3^19  '0b1000101010001101011001111011011' 31位
    # 在int以内的数，只要是3的m次方，一定会被M整除
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0
    # 3 递归 常规方法变式
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (n==1 or (n%3==0 and self.isPowerOfThree(n/3)))