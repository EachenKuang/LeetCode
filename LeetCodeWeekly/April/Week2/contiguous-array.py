# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

# 这是一道很有趣的题目，我们可以循序渐进来完成这道题


# 暴力法：
# 找到所有符合条件的子序列，保存，取最大值 O(n*n*n)
# 毫无疑问，超时了
class Solution1:
    def findMaxLength(self, nums: [int]) -> int:
        max_count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if 2 * nums[i:j].count(0) == len(nums[i:j]):
                    max_count = max(max_count, len(nums[i:j]))
        return max_count


# 使用的方法是求和+hashmap的方法，首先从头开始遍历，如果当前值是0就sum-1，否则就sum+1.这样如果得到了一个sum就知道在此之前出现了1的个
# 数和0的个数的差值。因此，当后面该sum再次出现的时候，我们就知道了这个差值再次出现，也就是说，从第一次这个差值出现和第二次这个差值出现之
# 间0和1的个数是一样多的。
#
# 因此我们需要一个map来保存0和1的差值。如果这个差值没出现过就给它赋值为它出现的索引。我们要求的就是当同样的差值出现的时候，两者之间的最大值。另外
# 注意，当这个差值再次出现的时候不要更新map。即我们的策略是只保存这个差值出现的第一个位置，只有这样我们才知道最长的连续子数组是多少。
class Solution2:
    def findMaxLength(self, nums: [int]) -> int:
        total_sum = 0
        index_map = {0: -1}
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                total_sum -= 1
            else:
                total_sum += 1
            if total_sum in index_map:
                res = max(res, i - index_map[total_sum])
            else:
                index_map[total_sum] = i
        return res


if __name__ == '__main__':
    solution1 = Solution1()
    # print(solution1.findMaxLength([0, 1]))
    assert 2 == solution1.findMaxLength([0, 1])
    assert 2 == solution1.findMaxLength([0, 1, 1])
    assert 2 == solution1.findMaxLength([0, 1, 1, 1])
    solution2 = Solution2()
    assert 2 == solution2.findMaxLength([0, 1])
    assert 2 == solution2.findMaxLength([0, 1, 1])
    assert 2 == solution2.findMaxLength([0, 1, 1, 1])