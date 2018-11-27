# https://leetcode.com/problems/magic-squares-in-grid/description/
class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        ans = 0
        for r in range(R-2):
            for c in range(C-2):
                if self.isMagix(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans
    def isMagix(a,b,c,d,e,f,g,h,i):
        if e!=5:
            return False
        else:
    def isMagix(self,a,b,c,d,e,f,g,h,i):
        if e!=5:
            return False
        else:
            return (set([a,b,c,d,e,f,g,h,i])==set(range(10))) and (a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g == 15)
"""
The center of magic square must be 5.
Another observation for other 8 numbers:
The even must be in the corner, and the odd must be on the edge.
And it must be in a order like "43816729" （clockwise or anticlockwise)
"""
class Solution:
    def numMagicSquaresInside(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(i, j):
            s = "".join(str(g[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return g[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        return sum(isMagic(i, j) for i in range(len(g) - 2) for j in range(len(g[0]) - 2) if g[i + 1][j + 1] == 5)


