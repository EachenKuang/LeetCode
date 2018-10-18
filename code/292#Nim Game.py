# https://leetcode.com/problems/nim-game/description/
# 题目很简单
# 对于先手，需要在第一次拿之后剩下是4的倍数就能赢。
# 先手拿完之后，不管后手怎么拿都能组成4的倍数，从而胜利。
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n%4 else False
        