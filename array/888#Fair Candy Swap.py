# https://leetcode.com/problems/fair-candy-swap/description/
class Solution:
    # 1 TLE 没通过
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A = sum(A)
        sum_B = sum(B)
        diff = sum_A-sum_B
        for i in set(A):
            if i-diff//2 in set(B):
                return [i,i-diff//2]
    # 2 用set
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """    
        sb = set(B)
        diff = (sum(B) - sum(A)) // 2
        for num in A:
            if num + diff in sb:
                return num, num + diff
        