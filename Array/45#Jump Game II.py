# https://leetcode.com/problems/jump-game-ii/description/
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
# 实际上这是一个求最短路径的题目
# 使用贪心算法，跳的越远越好。
class Solution(object):
	def jump1(self, nums):
		jumps = 0
		current_jump_max = 0
		previous_jump_max = 0

		for i in range(len(nums) - 1):
			current_jump_max = max(current_jump_max, i + nums[i])
			# Note 1
			if i == previous_jump_max:
				jumps += 1
				previous_jump_max = current_jump_max
			# Note 2
		return jumps

	def jump2(self, nums):
		ans, n = 0, len(nums)
		i, e = 0, 0
		while e < n - 1:
			p = e
			while i <= p:
				if i + nums[i] > e:
					e = i + nums[i]
				i += 1
			if p == e:
				return -1
			ans += 1
		return ans
