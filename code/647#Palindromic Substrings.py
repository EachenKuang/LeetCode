# https://leetcode.com/problems/palindromic-substrings/description/
class Solution:
	# 1 
	#  
	def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0        
        if not s:
            return ans        
        n = len(s)
        i = 0       
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            ans += (j - i) * (j - i + 1) // 2
            l = i - 1
            r = j            
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1            
            i = j       
        return ans
	# 2 
	# O(n)
    def countSubstrings2(self, S):
        """
        :type s: str
        :rtype: int
        """
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)//2 for v in manachers(S))