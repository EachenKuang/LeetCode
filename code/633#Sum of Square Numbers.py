# https://leetcode.com/problems/sum-of-square-numbers/description/
class Solution:
    """
    a**2+b**2 = c
    b**2 = c - a**2  右边是平方数且大于零
    那么可以遍历[0,c**.5+1]，看是否有书满足c-a**2是平方数
    """
    # 1 简洁
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N**.5)**2 == N        
        return any(is_square(c - a*a) for a in xrange(int(c**.5) + 1))
    # 2 
    # 更好理解的方法
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N**.5)**2 == N        
        for a in range(int(c**.5) + 1):
            if is_square(c - a*a):
                return True
        return False

    # 3
    # 使用部分数论的知识
    # https://www.maths.ed.ac.uk/~chris/NTh/Ch6_Sum2sq_Ch7_Fermat_descent.pdf
    def judgeSquareSum(self, c):
        if c % 4 == 3:
            return False
        
        i = 2
        s = 0
        while i*i <= c:
            s = 0
            while c % i == 0:
                if i % 4 == 3:
                    s += 1
                c //= i
            i += 1
            if s % 2 == 1:
                return False
        if c > 1 and c % 4 == 3:
            return False
        
        return True
