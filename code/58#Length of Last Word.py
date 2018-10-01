# https://leetcode.com/problems/length-of-last-word/description/
class Solution:
	# 1  one line
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if not s.split() else len(s.split()[-1])
    # 2
    
        