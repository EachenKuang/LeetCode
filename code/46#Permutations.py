# https://leetcode.com/problems/permutations/
"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

# 利用Python内部的数据结构
# Runtime: 60 ms, faster than 34.87% of Python3 online submissions for Permutations.
# Memory Usage: 13.2 MB, less than 5.23% of Python3 online submissions for Permutations.
class Solution1:
    def permute(self, nums: list[int]) -> list[list[int]]:
        from itertools import permutations
        return list(permutations(nums))

#
class Solution2:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        num = nums
        if not num:
            return []
        num.sort()
        ret = [[]]
        for n in num:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
        return ret

class Soluition3:
    def permute(nums):
        permutations = [[]]

        for head in nums:
            permutations = [rest[:i] + [head] + rest[i:] for rest in permutations for i in range(len(rest) + 1)]

        return permutations
