# https://leetcode.com/problems/sort-array-by-parity/description/
class Solution:
	# 1
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        让奇数在后，偶数在前
        两点法
        p1,p2 = 0,len(A)-1
        while p1<p2:
            while A[p1]%2==0 and p1<p2:
                p1+=1
            while A[p2]%2==1 and p1<p2:
                p2-=1
            A[p1],A[p2]=A[p2],A[p1]
        return A
    def sortArrayByParity(self, A):
        return sorted(A,key=lambda a:a%2)