# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n级的台阶总共有多少种跳法。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 示例 2：
#
# 输入：n = 7
# 输出：21
# 示例 3：
#
# 输入：n = 0
# 输出：1
# 提示：
#
# 0 <= n <= 100
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof

"""
f(n)
f(0) = 1
f(1) = 1
f(2) = f(0) + f(1)
f(n) = f(n-1) + f(n-2)
就是斐波那契
"""
class Solution:
    CONSTANT = 1000000007
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        f1 = f2 = 1
        for _ in range(2, n + 1):
            temp = f1 + f2
            f1 = f2 % self.CONSTANT
            f2 = temp % self.CONSTANT
        return f2 % self.CONSTANT