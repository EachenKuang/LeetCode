# https://leetcode.com/problems/positions-of-large-groups/description/
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        i = 0 # The start of each group
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans
                
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i, j, n, res = 0, 0, len(S), []
        
        while j < n:
            while j < n and S[i] == S[j]:
                j += 1
            if j - i >= 3:
                res.append((i, j-1))
            i = j
        return res