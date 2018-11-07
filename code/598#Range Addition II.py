# https://leetcode.com/problems/range-addition-ii/description/
class Solution:
    # 1
    def maxCount1(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        a,b=m,n
        for i in ops:
            a = min(i[0],a)
            b = min(i[1],b)
        return a*b
    # 2
    def maxCount2(self, m, n, ops):
    	if not ops:
            return m*n
        return min(op[0] for op in ops)*min(op[1] for op in ops)