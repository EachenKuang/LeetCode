# https://leetcode.com/problems/factorial-trailing-zeroes/description/
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 实际上是找1~n中有几个5的质因数
        # 分析
        # 1~10  2
        # 11~20 2
        # 21~30 25,30 3
        # 31~40 2
        # 41~50 45,50 3
        base = 5
        ans = 0
        while base <= n:
            ans += n//base
            base *=5
        return ans