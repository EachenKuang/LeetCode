# https://leetcode.com/problems/valid-perfect-square/description/
class Solution:
    # 1 常规方法 二分法
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 1
        high = num
        while low<=high:
            mid = low+(high-low)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                low=mid+1
            else:
                high=mid-1
        return False
    # 2 平方数都是1+3+5+...
    def isPerfectSqure(self, num):
    	i = 1
    	while num > 0:
    		num -= i
    		i += 2
    	return num==0