# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the
# product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
# (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for
# the purpose of space complexity analysis.)
#


# 方法一：先算乘法，再算除法
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        product = 1
        for num in nums:
            product *= num
        if all(nums):
            return [product // num for num in nums]
        else:
            # 如果有一个以上的0的情况下
            res_list = [0] * len(nums)
            if nums.count(0) == 1:
                zero_index = nums.index(0)
                nums[zero_index] = 1
                product = 1
                for num in nums:
                    product *= num
                res_list[zero_index] = product
            return res_list


# 方法二：（题目要求不用除法）,方法一的改进
from functools import reduce
class Solution2:

    def multiply(self, a, b):
        return a * b

    def productExceptSelf(self, nums: [int]) -> [int]:
        if all(nums):
            product = reduce(self.multiply, nums)
            return [product // num for num in nums]
        else:
            res_list = [0] * len(nums)
            if nums.count(0) == 1:
                zero_index = nums.index(0)
                nums[zero_index] = 1
                product = reduce(self.multiply, nums)
                res_list[zero_index] = product
            return res_list


class Solution3:
    def productExceptSelf(self, nums: [int]) -> [int]:
        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        r = 1
        for i in reversed(range(len(nums))):
            ans[i] = ans[i] * r
            r *= nums[i]

        return ans
if __name__ == '__main__':
    solution = Solution()
    solution2 = Solution2()
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([1, 2, 3, 4, 0]) == [0, 0, 0, 0, 24]
    assert solution2.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution2.productExceptSelf([1, 2, 3, 4, 0]) == [0, 0, 0, 0, 24]

