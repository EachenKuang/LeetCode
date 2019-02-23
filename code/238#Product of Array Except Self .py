# https://leetcode.com/problems/product-of-array-except-self/description/
"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)

"""
from functools import reduce
class Solution:
    # 1
    # # with division
    # 用所有数的积来进行计算
    # 当nums中有0时，会出现问题。
    # 可以处理
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mutifly(a, b):
            return a*b
        if all(nums):
            product = reduce(mutifly, nums)
            return [product//n for n in nums]
        else:
            ret = [0]*len(nums)
            if nums.count(0)==1:
                i = nums.index(0)
                nums[i]=1
                ret[i] = reduce(mutifly, nums)
            return ret
    # 2
    def productExceptSelf2(self, nums):
        p = 1
        n =len(nums)
        ret = []
        for i in range(0, n):
            ret.append(p)
            p = p*nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            ret[i] = ret * p
            p = p * nums[i]
        return ret


if __name__ == '__main__':
    t = Solution()
    input_array = [1,2,3,4]
    output_array = [24,12,8,6]
    assert t.productExceptSelf(input_array)==output_array

    input_array = [1, 2, 3, 0]
    output_array = [0, 0, 0, 6]
    assert t.productExceptSelf(input_array) == output_array