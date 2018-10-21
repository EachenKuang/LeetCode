# https://leetcode.com/problems/sum-of-two-integers/description/
class Solution: 
    # 1 trick
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        tmp = [a, b]
        return sum(tmp)
    # 2 
    def getSum(self, a, b):
        MOD     = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            a, b = (a ^ b) & MOD, ((a & b) << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT

# https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently