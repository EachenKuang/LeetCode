# https://leetcode.com/problems/monotonic-array/description/
class Solution:
    # 1
    def isMonotonic(self, A):
        is_reverse = False
        if A[0]>A[-1]:
            is_reverse=True
        B = sorted(A,reverse=is_reverse)
        return A==B
    # 2
    def isMonotonic(self, A):
        return A==sorted(B,reverse=True if A[0]>A[-1] else False)
    # 3
    def isMonotonic(self, A):
        if not A or len(A) < 2:
            return True        
        if A[0] <= A[-1]:
            left = A[0]
            for x in A:
                if x >= left:
                    left = x
                else:
                    return False
        else:
            left = A[0]
            for x in A:
                if x <= left:
                    left = x
                else:
                    return False
        
        return True