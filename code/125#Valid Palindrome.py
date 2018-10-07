# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 实际上是判断一个一个字符串的英文字母字串是否是回文
        processedString = []
        for c in s:
            if c.isalnum():
                processedString.append(c.lower())
            
        l = len(processedString)
        for i in range(0, l//2):
            if processedString[i] != processedString[l-1-i]:
                return False
            
        return True
			