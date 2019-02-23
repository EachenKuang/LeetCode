# https://leetcode.com/problems/4sum-ii/description/
"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
class Solution1:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        cnts = 0
        dd = {}
        aa = {}
        bb = {}
        cc = {}
        for a in A:
            aa[a] = aa.get(a, 0) + 1
        for b in B:
            bb[b] = bb.get(b, 0)+1
        for c in C:
            cc[c] = cc.get(c, 0) + 1
        for d in D:
            dd[d] = dd.get(d, 0) + 1
        ab = {}
        for a, av in aa.items():
            for b, bv in bb.items():
                ab[a+b] = ab.get(a+b, 0) + av*bv

        for c, cv in cc.items():
            for d, dv in dd.items():
                if -c-d in ab:
                    cnts += ab[-c-d] * cv * dv
        return cnts

class Solution2:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)