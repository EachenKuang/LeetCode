# https://leetcode.com/problems/expressive-words/description/
class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """        
        return sum(self.check(S, W) for W in words)
    def check(self, S, W):
        i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
        while i < n and j < m:
            if S[i] != W[j]: return False
            while i2 < n and S[i2] == S[i]: i2 += 1
            while j2 < m and W[j2] == W[j]: j2 += 1
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j): return False
            i, j = i2, j2
        return i == n and j == m