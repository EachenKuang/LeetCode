# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
# which is more subtle.

# 暴力破解法
import sys


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        n = len(nums)
        max_sum = -sys.maxsize
        for i in range(n):
            res_sum = 0
            for j in range(i, n):
                res_sum += nums[j]
                max_sum = max(max_sum, res_sum)
        return max_sum


# 分而治之法
# time(O(n*logn))
import sys


class Solution1:
    def maxSubArray(self, nums: [int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: [int], l: int, r: int):
        if l > r:
            return -sys.maxsize
        mid = (l + r) // 2
        left = self.helper(nums, l, mid - 1)
        right = self.helper(nums, mid + 1, r)
        left_suffix_max_sum = right_prefix_max_sum = 0
        res_sum = 0
        for i in reversed(range(l, mid)):
            res_sum += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum, res_sum)
        res_sum = 0
        for i in range(mid + 1, r + 1):
            res_sum += nums[i]
            right_prefix_max_sum = max(right_prefix_max_sum, res_sum)
        cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
        return max(cross_max_sum, left, right)


# 动态规划法
# Q(list, i) 表示 list 中以索引 i 结尾的情况下最大子序列和
# 可以得到递推公式：
# Q(list, i) = Math.max(0, Q(list, i - 1)) + list[i]
class Solution2:
    def maxSubArray(self, nums: [int]) -> int:
        n = len(nums)
        max_sum_ending_curr_index = max_sum = nums[0]
        for i in range(1, n):
            max_sum_ending_curr_index = max(max_sum_ending_curr_index + nums[i], nums[i])
            max_sum = max(max_sum_ending_curr_index, max_sum)

        return max_sum


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    solution1 = Solution1()
    assert solution1.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    solution2 = Solution2()
    assert solution2.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
