# https://leetcode.com/problems/valid-mountain-array/description/
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1

    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3: return False
        if A[0] >= A[1]: return False
        climb = True
        for a,b in zip(A,A[1:]):
            if climb:
                if a<b: continue
                if a>b: climb = False; continue
                return False
            else:
                if a>b: continue
                return False
        return not climb