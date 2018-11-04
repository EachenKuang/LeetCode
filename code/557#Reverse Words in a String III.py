# https://leetcode.com/submissions/detail/187303513/
class Solution:
    # 1
    # one line
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(word[::-1] for word in s.split())