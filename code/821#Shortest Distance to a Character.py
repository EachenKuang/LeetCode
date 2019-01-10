# https://leetcode.com/problems/shortest-distance-to-a-character/
"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        ans = [0 if i == C else n for i in S]
        for i in range(n-1):
            ans[i+1] = min(ans[i+1],ans[i]+1)
        for j in range(n-1)[::-1]:
            ans[j] = min(ans[j],ans[j+1]+1)
        return ans


