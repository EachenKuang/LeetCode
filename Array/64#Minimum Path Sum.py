# https://leetcode.com/problems/minimum-path-sum/description/
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

    def minPathSum2(self, grid):
        if grid == None or grid == []:
            return None
        n = len(grid[0])
        m = len(grid)

        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]

        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]

        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                if dp[j - 1] < dp[j]:
                    dp[j] = dp[j - 1] + grid[i][j]
                else:
                    dp[j] = dp[j] + grid[i][j]

        return dp[-1] if dp else 0