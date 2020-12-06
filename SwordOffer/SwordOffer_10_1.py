# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
# 
# F(0) = 0, F(1)= 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
# 
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
# 
# 示例 1：
# 
# 输入：n = 2
# 输出：1
# 示例 2：
# 
# 输入：n = 5
# 输出：5
# 
# 
# 提示：
# 
# 0 <= n <= 100
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
class Solution:

    CONSTANT = 1000000007

    def fib(self, n: int) -> int:
        """
        也可以使用数组作为备忘录，自底向上，非递归
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        f1 = f2 = 1
        for _ in range(3, n+1):
            temp = f1 + f2
            f1 = f2 % self.CONSTANT
            f2 = temp % self.CONSTANT
        return f2 % self.CONSTANT

    def fib2(self, n: int) -> int:
        """
        简单递归方法，自顶向下
        """
        if n < 2:
            return n
        first = self.fib(n - 1) % self.CONSTANT
        second = self.fib(n - 2) % self.CONSTANT
        return (first + second) % self.CONSTANT


if __name__ == '__main__':
    solution = Solution()
    assert solution.fib(0) == 0
    assert solution.fib(1) == 1
    assert solution.fib(2) == 1
    assert solution.fib(3) == 2
    assert solution.fib(4) == 3
    assert solution.fib(5) == 5

    assert solution.fib2(0) == 0
    assert solution.fib2(1) == 1
    assert solution.fib2(2) == 1
    assert solution.fib2(3) == 2
    assert solution.fib2(4) == 3
    assert solution.fib2(5) == 5
