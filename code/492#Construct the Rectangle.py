# https://leetcode.com/problems/construct-the-rectangle/description/
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # 
        bondary = int(area**0.5)
        for i in range(bondary,0,-1):
            if area%i == 0:
                return [area//i,i]