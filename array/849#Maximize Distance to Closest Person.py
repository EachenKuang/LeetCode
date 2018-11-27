# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
class Solution:
    # 1
    # [1,0,0,0,1] output:2
    # [0,0,0,1] outpu:#
    # [0,0,0,1,0,0] output:3
    # 找连续的0
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_dis = 0 
        cur_dis = 0
        for value in seats:
            if value==0:
                cur_dis+=1
            else:
                max_dis = max(max_dis,cur_dis)
                cur_dis = 0
        head_dis = seats.index(1)
        tail_dis = cur_dis
        max_dis = ((max_dis+1)//2,head_dis,tail_dist)
        return max_dis
    # 2
    def maxDistToClosest(self, seats):
        start, end = 0,len(seats) - 1
        while seats[start] == 0:
            start += 1
        while seats[end] == 0:
            end -= 1
        max_dist, dist = 0, 0

        for i in range(start, end+1):
            if seats[i] == 1:
                if dist > max_dist:
                    max_dist = dist
                dist = 0
            else:
                dist += 1
        return max(math.ceil(max_dist/2), start, len(seats) - end -1)
