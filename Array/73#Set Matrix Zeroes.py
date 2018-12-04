# https://leetcode.com/problems/set-matrix-zeroes/description/
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    # 1
    # force
    # wrong
    # 一开始理解错题意，以为只是将0周围的数字变成0即可。
    # 后面发现是将这一行以及这一列的所有数字变成0
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        point_set = set()
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    if i >= 1:
                        point_set.add((i-1, j))
                    if i <= rows-2:
                        point_set.add((i+1, j))
                    if j >= 1:
                        point_set.add((i, j-1))
                    if j <= columns-2:
                        point_set.add((i, j+1))
        for (r, c) in point_set:
            matrix[r][c] = 0

    def setZeroes2(self, matrix):
        # First row has zero?
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n
    # 3
    def setZeroes3(self, matrix):

        if not matrix or not matrix[0]:
            return

        h = len(matrix)
        w = len(matrix[0])

        rows_to_remove = set()
        cols_to_remove = set()

        for i in range(h):
            if i not in rows_to_remove:
                for j in range(w):
                    if matrix[i][j] == 0:
                        rows_to_remove.add(i)
                        cols_to_remove.add(j)

        for i in rows_to_remove:
            for j in range(w):
                matrix[i][j] = 0

        for j in cols_to_remove:
            for i in range(h):
                matrix[i][j] = 0