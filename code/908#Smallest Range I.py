class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # return 0 if max(A)-min(A)< K*2 else max(A) - min(A) - K*2
        return max(0, max(A) - min(A) - K*2)