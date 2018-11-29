# https://leetcode.com/problems/max-area-of-island/description/
class Solution:
    def maxAreaOfIsland(self, grid):
        max_size = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j, size):
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] in (-1, 0):
                return
            size[0] += 1
            grid[i][j] = -1
            for direction in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                dfs(i + direction[0], j + direction[1], size)
        for i in range(rows):
            for j in range(cols):
                size = [0]
                dfs(i, j, size)
                max_size = max(max_size, size[0])
        return max_size