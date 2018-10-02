# https://leetcode.com/problems/sqrtx/description/
class Solution:
	# 1 标准版
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        while low<=high:
            mid = low+(high-low)//2
            if x==mid**2:
                return mid
            elif x<mid**2:
                high=mid-1
            else:
                low=mid+1
        return high
    # 2 精确版
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
        	return 0
        low = 1
        high = x
        while low<=high:
            mid = low+(high-low)//2
            if x//mid < mid:
                high = mid - 1
            else:
            	if x//(mid+1)<mid+1:
                	return mid
                low=mid+1