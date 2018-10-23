# https://leetcode.com/problems/nth-digit/description/
"""
1位数  9*1
2位数  90*2
3位数  900*3
4位数  9000*4
bit = 1 =>+1
base = 9  =>*10
"""
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit = 1
        base = 9
        while n>bit*base:
            n -= bit*base
            bit += 1
            base *= 10
        order = n//bit+1
        num_bit = n%bit
        start = 10**(bit-1)
        which = start + order -1
        ret = str(which)[num_bit-1] if num_bit>0 else str(which-1)[-1]
        return int(ret)
