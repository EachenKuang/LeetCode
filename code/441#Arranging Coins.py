# https://leetcode.com/problems/arranging-coins/description/
class Solution(object):
	# 1 公式法
	# h*(h+1)/2<n =>  h^2+h-2n<0
	# h ≤ (sqrt(8n + 1) -1)/2
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(8 * n + 1)-1)/2)
    # 2 二分法
	def arrangeCoins2(self, n) 
    	target=2*n        
        low,high=1,n
        
        while low<=high:
            mid=(low+high)/2
            ans=mid*(mid+1)
            if ans<target:
                low=mid+1
            if ans>target:
                high=mid-1
            if ans==target:
                return mid
        return high