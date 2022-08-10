# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#
# 示例 1:
#
# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#  
#
# 说明：
#
# 用返回一个整数列表来代替打印
# n 为正整数
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        """
        简单来说，就是打印 1~10^n-1
        """
        return [i for i in range(1, 10**n)]

    # 其实应该考虑是的大数的存储问题，不论是short，int, long 都是有其最大值的，所以需要考虑用字符串存储。
    # 实际上是一个全排列。
    def printNumbers(self, n: int) -> List[str]:
        pass
    