# https://leetcode.com/problems/flipping-an-image/description/
class Solution:
    # in-place reverse
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for r in range(len(A)):
            for c in range(len(A[0])):
                # A[r][c] = 1-A[r][c]
                A[r][c] ^= 1 
        for r in range(len(A)):
            A[r].reverse()
        return A
    # another space
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """     
        reverse = []
        for i in A:
            temp = []
            for j in reversed(i):
                if(j==0):
                    temp.append(1)
                else:
                    temp.append(0)
            reverse.append(temp)
        return (reverse)
        