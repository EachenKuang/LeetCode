# https://leetcode.com/problems/number-of-segments-in-a-string/description/
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())