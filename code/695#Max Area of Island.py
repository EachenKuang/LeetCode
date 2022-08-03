# https://leetcode.com/problems/max-area-of-island/description/
import collections
from typing import List


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

    # 递归方法使用
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        # 递归终止
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return self.dfs(grid, i-1, j) + self.dfs(grid, i+1, j) + self.dfs(grid, i, j-1) + self.dfs(grid, i, j+1) + 1
        
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                ans = max(ans, self.dfs(grid, i, j))
        return ans

    # 栈 DFS

    def maxAreaOfIsland3(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                stack = [(i,j)]
                cur = 0
                while stack:
                    cur_i, cur_j = stack.pop()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        stack.append((next_i, next_j))
                ans = max(ans, cur)
        return ans

    # 队列 BFS
    # 使用队列来存储，相当于是广度优先
    def maxAreaOfIsland4(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                q = collections.deque([(i, j)])
                cur = 0
                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        q.append((next_i, next_j))
                ans = max(ans, cur)
        return ans




            