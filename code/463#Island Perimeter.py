# https://leetcode.com/problems/island-perimeter/description/
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 1 
        # 思考：
        # 只有一个岛屿，所以不需要考虑多个单岛屿
        # 那么只需要找到公式即可
        # 
        # Input:
        # [[0,1,0,0],
        #  [1,1,1,0],
        #  [0,1,0,0],
        #  [1,1,0,0]]
        # Output: 16
        # 一共7个1*1，共28条边，有6条边重合，减去6*2=12
        # 结果为7&4-2*6=16   sum = 4n-2l
        # 注意分情况：在边上的时候
        l = n = 0
        a = len(grid)
        b = len(grid[0])
        for i in range(a):
            for j in range(b):
                if grid[i][j]==1:
                    n += 1
                    if i< a-1 and j < b-1:
                        l = l + grid[i][j + 1] + grid[i + 1][j]
                    elif i < a-1:
                        l += grid[i+1][j]
                    elif j < b-1:
                        l += grid[i][j + 1]

        s = 4*n-2*l
        return s
