# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
# 示例:
#
# 现有矩阵 matrix 如下：
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定target=5，返回true。
#
# 给定target=20，返回false。
#
# 限制：
# 0 <= n <= 1000
# 0 <= m <= 1000

from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        第一种方法
        一行一行遍历
        """
        if not matrix or not matrix[0]:
            return False
        col_length = len(matrix[0])
        line_length = len(matrix)
        for i in range(line_length):
            for j in range(col_length):
                if matrix[i][j] == target:
                    return True
        return False

    def findNumberIn2DArray1_2(self, matrix: List[List[int]], target: int) -> bool:
        """
        方法一更加pythonic的方法
        """
        for line in matrix:
            for col in line:
                if col == target:
                    return True
        return False

    def findNumberIn2DArray2(self, matrix: List[List[int]], target: int) -> bool:
        """
        第二种方法
        在方法一上有所改进，从左下角角开始遍历
        """
        if not matrix and len(matrix) == 0 and len(matrix[0]) == 0:
            return False
        col_length = len(matrix[0])
        line_length = len(matrix)
        i = line_length - 1
        j = 0
        while j < col_length and i >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    input_items = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    output_items = solution.findNumberIn2DArray(input_items, 3)
    assert output_items is True
    output_items1_2 = solution.findNumberIn2DArray1_2(input_items, 3)
    assert output_items1_2 is True
    output_items2 = solution.findNumberIn2DArray2(input_items, 5)
    assert output_items2 is True
