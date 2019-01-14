# https://leetcode.com/problems/largest-triangle-area/
"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
#         candidate_points = [
#         max(points, key=lambda p:p[0]),
#         max(points, key=lambda p:p[1]),
#         min(points, key=lambda p:p[0]),
#         min(points, key=lambda p:p[1])]
        
#         # S=1/2[(x1y2-x2y1)+(x2y3-x3y2)+(x3y1-x1y3)]
#         def area(pointA, pointB, pointC):
#             return 1/2.0*((pointA[0]*pointB[1] - pointB[0]*pointA[1])
#                         +(pointB[0]*pointC[1] - pointC[0]*pointB[1])
#                         +(pointC[0]*pointA[1] - pointA[0]*pointC[1]))
#         return max(
#             area(candidate_points[0],candidate_points[1],candidate_points[2]),
#             area(candidate_points[0],candidate_points[2],candidate_points[3]),
#             area(candidate_points[1],candidate_points[2],candidate_points[3]),
#             area(candidate_points[0],candidate_points[1],candidate_points[3])
#         )
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
            for i, j, k in itertools.combinations(points, 3))