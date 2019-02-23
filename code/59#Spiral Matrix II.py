# https://leetcode.com/problems/spiral-matrix-ii/description/
"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    # 1
    # 对应54#Spiral Matrix的逆运算
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        elif n ==1:
            return [[1]]
        seen = [[False] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(1,n*n+1):
            seen[r][c] = i
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return seen

    # 2
    # 更清晰的一种写法
    def generateMatrix2(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0] * n for _ in range(n)]
        i = j = d = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x in range(1, n * n):
            ret[i][j] = x
            nextDir = dirs[d]
            while (i + nextDir[0] == n) or (i + nextDir[0] == -1) or \
                  (j + nextDir[1] == n) or (j + nextDir[1] == -1) or \
                  ret[i + nextDir[0]][j + nextDir[1]] != 0:
                        d = (d + 1) % 4
                        nextDir = dirs[d]
            i += nextDir[0]
            j += nextDir[1]
        ret[i][j] = n * n
        return ret