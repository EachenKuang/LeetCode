# https://leetcode.com/problems/word-pattern/description/
class Solution:
    # 1
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))
    # 2
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)