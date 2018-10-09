# https://leetcode.com/problems/excel-sheet-column-number/description/
class Solution:
    # 1 常规法
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = 0
        base = 1
        for i in s[::-1]:
            res += (alpha.index(i)+1) * base
            base *= 26
        return res
    # 2 一行Python法
    # 利用reduce函数与lambda
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: x*26 + y, [ord(c) - ord('A') + 1 for c in s])