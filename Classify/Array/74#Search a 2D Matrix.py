# https://leetcode.com/problems/search-a-2d-matrix/description/
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution:
    # 从右上角开始
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        column = len(matrix[0])
        i,j=0,column-1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

    # 用两个二分法来找出结果
    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        if not matrix[0]: return False
        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if matrix[mid][0] < target:
                left = mid
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True

        index = left
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[index][mid] < target:
                left = mid + 1
            elif matrix[index][mid] > target:
                right = mid - 1
            else:
                return True
        return False