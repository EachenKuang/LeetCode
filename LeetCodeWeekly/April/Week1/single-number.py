# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
#
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4
from functools import reduce


# 方法一：
# 直接使用异或操作，因为两个相同的数异或的结果是0，0和任何数异或的结果为任何数
# 4 ^ 4 = 0  and 0 ^ n = n
# 所以，对所有数进行连续异或操作就可以得出单独的那个数
class Solution:
    def notOr(self, a, b):
        return a ^ b

    def singleNumber(self, nums: [int]) -> int:
        return reduce(self.notOr, nums)

# 方法二：
# 放入字典中，作为计数器，得出最后数量为1的那个key即可
# 这里可以引入Counter这个库
# from collections import Counter


if __name__ == '__main__':
    solution = Solution()
    assert solution.singleNumber([2, 2, 1]) == 1
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
