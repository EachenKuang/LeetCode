# https://leetcode.com/problems/keyboard-row/description/
class Solution:
    # 1
    # 利用集合方法issubset()
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = "qwertyuiopQWERTYUIOP"
        line2 = "asdfghjklASDFGHJKL"
        line3 = "zxcvbnmZXCVBNM"
        res = []
        for word in words:
            s = set(word)
            if s.issubset(line1) or s.issubset(line2) or s.issubset(line3):
                res.append(word)
        return res