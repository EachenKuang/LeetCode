# https://leetcode.com/problems/rectangle-overlap/
"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
"""
class Solution1:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # return True only when [Re1x1,Re1x2] [Re2x1,Re2x2]  overlap and [Re1y1,Re1y2]  [Re2y1,Re2y2]
        if (rec1[0] <= rec2[0] < rec1[2] or rec2[0] <= rec1[0] < rec2[2]) and (rec1[1] <= rec2[1] < rec1[3] or rec2[1] <= rec1[1] < rec2[3] ):
            return True
        return False
class Solution2:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,y1,x2,y2 = rec1
        x3,y3,x4,y4 = rec2
        if x1>=x4 or x2<=x3 or y1>=y4 or y2<=y3:
            return False
        else:
            return True