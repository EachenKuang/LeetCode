# https://leetcode.com/problems/assign-cookies/description/
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = j = 0
        res = 0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                res +=1
                i += 1
            j += 1
        return res