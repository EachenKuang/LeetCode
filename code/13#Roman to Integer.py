# https://leetcode.com/problems/roman-to-integer/description/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        dic_str = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        pre = 0
        for i in range(len(s)-1, -1, -1):
            tmp = dic_str[s[i]]
            if tmp < pre:
                ans -= tmp
            else:
                ans += tmp
            pre = tmp
        return ans