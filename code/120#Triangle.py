# https://leetcode.com/problems/triangle/
"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
class Solution1:

    def minimumTotal(self, triangle):
        from functools import reduce
        def combine_rows(lower_row, upper_row):
            return [upper + min(lower_left, lower_right)
                    for upper, lower_left, lower_right in
                    zip(upper_row, lower_row, lower_row[1:])]
        return reduce(combine_rows, triangle[::-1])[0]

class Solution2:
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i]) - 1, -1, -1):
                small = min(triangle[i+1][j], triangle[i+1][j+1])
                triangle[i][j] += small
        return triangle[0][0]