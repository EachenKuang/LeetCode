# https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

# 请写一个函数，求任意第n位对应的数字。

#  

# 示例 1：

# 输入：n = 3
# 输出：3
# 示例 2：

# 输入：n = 11
# 输出：0
#  

# 限制：

# 0 <= n < 2^31
# 注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/



class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        这题还是需要找规律
        1~9   1位数   数字数量 9 长度总和 9
        10~99  2位数  数字数量 90 长度总和 90*2
        100~999  3位数  数字数量 900 长度总和 900*3
        通过循环，找出 n 位于哪个区间，从哪个数开始，最终坐落在哪个数上，然后根据位数取余，知道是第几位上。
        """
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.



