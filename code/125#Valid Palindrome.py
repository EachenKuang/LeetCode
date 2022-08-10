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

    def isPalindrome2(self, s):
            """
            :type s: str
            :rtype: bool
            """
            import re
            s = s.lower()
            s1 = re.findall(r'[a-z0-9]', s)
            s2 = "".join(s1)
            # 使用字符串切片反转
            return s2[::-1] == s2
