# https://leetcode.com/problems/detect-capital/description/
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if word.islower() or word.isupper():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        return False
