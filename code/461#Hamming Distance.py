# https://leetcode.com/problems/hamming-distance/description/
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #  1 
        # beat 99%
        # 先异或两个数，然后计算几个1
        # 可以见191#Number of 1 Bits.py
        # 怎么计算二进制数中的1
        sum = x^y
        count = 0
        while sum>0:
            sum&=sum-1
            count+=1
        return count