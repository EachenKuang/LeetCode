class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        m = 0
        n = 1
        if N == 0:
            return 0
        for i in range(N-1):
            temp = m + n
            m = n
            n = temp
        return n