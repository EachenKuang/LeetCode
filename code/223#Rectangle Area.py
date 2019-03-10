# https://leetcode.com/problems/rectangle-area/
"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
"""
class Solution1:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (C-A)*(D-B) + (G-E)*(H-F) - max(0,min(G,C)-max(A,E))*max(0,min(D,H)-max(B,F))


class Solution2:
    def computeArea(self, A: 'int', B: 'int', C: 'int', D: 'int', E: 'int', F: 'int', G: 'int', H: 'int') -> 'int':
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        return area1 + area2 - self.find_overlap(A, C, E, G) * self.find_overlap(F, H, B, D)

    def find_overlap(self, A, C, E, G):
        if E <= A:
            if G <= A:
                return 0
            elif G <= C:
                return G - A
            return C - A
        elif E <= C:
            if G >= C:
                return C - E
            return G - E
        else:
            return 0