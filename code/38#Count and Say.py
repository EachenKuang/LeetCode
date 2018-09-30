# https://leetcode.com/problems/count-and-say/description/
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        if n == 2: return "11"
        prev = "11"
        for i in range(3, n+1):
            res = ""
            ct = 1
            for j in range(1, len(prev)):
                if prev[j] != prev[j-1]:
                    res = res + str(ct) + prev[j-1]
                    ct = 1
                else:
                    ct += 1
            res = res + str(ct) + prev[j]
            prev = res
        return res