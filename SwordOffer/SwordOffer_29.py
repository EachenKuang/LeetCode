# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#  
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
#
# 限制：
#
# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        [[1,2,3],[4,5,6],[7,8,9]]
        (0,0),(0,1),(0,2),(1,2),(2,2),(2,1),(2,0),(1,0)

        四种情况：
        - 向右走 y+1
        - 向下走 x+1
        - 向左走 y-1
        - 向上走 x-1

        """
        if len(matrix) == 0:
            return []
        direction = 0
        i = j = 0
        result = [matrix[i][j]]
        corner_x_min = 0
        corner_x_max = len(matrix) - 1
        corner_y_min = 0
        corner_y_max = len(matrix[0]) - 1
        while corner_x_min <= corner_x_max and corner_y_min <= corner_y_max:
            if direction == 0:
                if j + 1 > corner_y_max:
                    direction = (direction + 1) % 4
                    corner_x_min += 1
                else:
                    j += 1
                    result.append(matrix[i][j])
            elif direction == 1:
                if i + 1 > corner_x_max:
                    direction = (direction + 1) % 4
                    corner_y_max -= 1
                else:
                    i += 1
                    result.append(matrix[i][j])
            elif direction == 2:
                if j - 1 < corner_y_min:
                    direction = (direction + 1) % 4
                    corner_x_max -= 1
                else:
                    j -= 1
                    result.append(matrix[i][j])
            else:
                if i - 1 < corner_x_min:
                    direction = (direction + 1) % 4
                    corner_y_min += 1
                else:
                    i -= 1
                    result.append(matrix[i][j])
        return result

    def spiralOrder_2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])  # left to right
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])  # top to bottom
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])  # right to left
            b -= 1
            if t > b:
                break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])  # bottom to top
            l += 1
            if l > r:
                break
        return res


    def spiralOrder_3(self, matrix: List[List[int]]) -> List[int]:
        """
        黑科技
        每次都打印第一层，然后反转数组
        """
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


if __name__ == '__main__':
    solution = Solution()
    test_suits = [
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1]],
        []
    ]
    results = [
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
        [1],
        []
    ]
    for method in (solution.spiralOrder, solution.spiralOrder_2, solution.spiralOrder_3):
        for test_suit, result in zip(test_suits, results):
            assert result == method(test_suit)
