# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    # 1
    # 暴力法
    # Time Limit Exceeded 
    def maxArea(self, height):
        ret = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)): 
                ret = max(ret,min(height[i],height[j])*(j-i))
        return ret
    def maxArea(self, height):
    	lpoint,rpoint=0,len(height)-1
    	max_area = 0
    	while lpoint<rpoint:
    		max_area=max(max_area,(rpoint - lpoint)*min(height[rpoint],height[lpoint]))
    		if height[rpoint]>height[lpoint]:
    			lpoint+=1
    		else:
    			rpoint-=1
    	return max_area

