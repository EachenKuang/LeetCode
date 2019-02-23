# https://leetcode.com/problems/transpose-matrix/description/
class Solution:
    # 1 
    # 常规法
    # O(mn)
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        trans = []
        for c in range(len(A[0])):
            temp = []
            for r in range(len(A)):
                temp.append(A[r][c])
            trans.append(temp)
        return trans
    # 2
    # 提前构造矩阵，利用变化式 a[i][j] = b[j][i]
    def transpose(self, A):
        M,N = len(A),len(A[0])   
        trans = [[None for m in range(M)] for n in range(N)] 
        for i in range(M):
            for j in range(N):
                trans[j][i] = trans[i][j]     
        return trans