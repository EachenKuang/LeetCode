# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
#
#  
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#  
#
# 提示：
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        这个方法会超时，不正确
        """
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        res = 1
        while n > 0:
            res *= x
            n -= 1
        return res

    def myPow_1(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

    # 这个就是快速幂的递归方法
    # 实际上可以不用考虑底数为负数的情况
    def myPow3(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1/x, -n)
        
        if n % 2:
            return x * self.myPow(x, n-1)
        else:
            temp = self.myPow(x, n//2)
            return temp * temp
