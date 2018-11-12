# https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution1:
    def validPalindrome(self, s):
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return self.isValidPalindrome(s,l,r-1) or self.isValidPalindrome(s,l+1,r)
            l+=1
            r-=1
        return True
    
    def isValidPalindrome(self, s, l, r):
        while l < r :
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

class Solution2:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = s[::-1]
        if a == s:
            return True
        else:
            for i in range(len(s)):
                if s[i] != a[i]:
                    break

            for j in i, len(s)-i-1:        
                b = s[:j]+s[j+1:]
                if b == b[::-1]:
                    return True
            
        return False