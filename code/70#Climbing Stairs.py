# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    # 1
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        a,b=1,2
        for i in range(3,n+1):
            temp=a+b
            a,b=b,temp
        return temp
    # 2 使用递归，可能会溢出