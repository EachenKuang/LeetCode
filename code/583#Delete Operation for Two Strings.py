# https://leetcode.com/problems/delete-operation-for-two-strings/description/
# 1 Runtime Error
class Solution:
    def minDistance(self, word1, word2):
    	return len(word1) + len(word2) - 2 * self.lcs(word1, word2, len(word1),len(word2))
    def lcs(self,s1,s2,m,n):
    	if m==0 and n==0:
    		return 0
    	if (s1[m-1]==s2[n-1]):
    		return 1 + self.lcs(s1,s2,m-1,n-1)
    	else:
    		return max(self.lcs(s1,s2,m,n-1), self.lcs(s1,s2,m-1,n))
# 2
# add memory
class Solution:
	def minDistance(self, word1, word2):
		def lcs(s1,s2,m,n,memo):
			if m==0 and n==0:
				return 0
			if memo[m][n]>0:
				return memo[m][n]
			if (s1[m-1]==s2[n-1]):
				memo[m][n] = 1 + self.lcs(s1,s2,m-1,n-1,memo)
			else:
				memo[m][n] = max(lcs(s1,s2,m,n-1), lcs(s1,s2,m-1,n),memo)
			return memo[m][n]
		memo = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
		return len(word1) + len(word2) - 2 * lcs(word1, word2, len(word1),len(word2), memo)
# 3 dict moemo
class Solution:
	def minDistance(self, A, B):
	    memo = {}
	    def dp(i, j):
	        if (i, j) not in memo:
	            if i == len(A) or j == len(B):
	                ans = len(A) + len(B) - i - j
	            elif A[i] == B[j]:
	                ans = dp(i+1, j+1)
	            else:
	                ans = 1 + min(dp(i+1, j), dp(i, j+1))
	            memo[i, j] = ans
	        return memo[i, j]
	    return dp(0, 0)
# 4 无递归
class Solution:
    def minDistance(self, word1, word2):
        L1, L2 = len(word1), len(word2)
        d = [[0] * (L2 + 1) for _ in range(L1 + 1)]

        for i, l1 in enumerate(word1):
            for j, l2 in enumerate(word2):
                if l1 == l2:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1])
        
        len_lcs = d[L1-1][L2-1]
        return L1 + L2 - 2 * len_lcs


# 5 
class Solution:
    def minDistance(self, word1, word2):
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) + len(word2)
        
        a = [0] * len(word1)
        b = [0] * len(word1)
        
        for i in range(len(word2)):
            b[0] = 1 if word2[i] == word1[0] else a[0]
            for j in range(1, len(word1)):
                b[j] = a[j-1] + 1 if word2[i] == word1[j] else max(b[j-1], a[j])
            a, b = b, a
        
        return len(word1) + len(word2) - 2 * max(a[-1], b[-1])