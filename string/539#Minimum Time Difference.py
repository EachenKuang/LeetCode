# https://leetcode.com/problems/minimum-time-difference/description/
#24*60 = 1440 种情况
class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def diff(tp1,tp2):
            return 60*(int(tp1[0:2])-int(tp2[0:2]))+int(tp1[3:])-int(tp2[3:])

        if len(set(timePoints))<len(timePoints):
            return 0
        
        timePoints.sort()
        mini = 1440
        for i in range(1,len(timePoints)):
            mini = min(diff(timePoints[i],timePoints[i-1]),mini)
        mini = min(mini,diff(timePoints[0],timePoints[-1])+1440)
        return mini