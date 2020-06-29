# https://leetcode.com/problems/toeplitz-matrix/description/
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)        
        for i in range(m-1):
            if matrix[i][:-1]!=matrix[i+1][1:]:
                return False
        return True

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                
        return True

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False
        return True
    def isToeplitz Matrix(self, m):
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(m[:-1], m[1:]))