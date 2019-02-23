# https://leetcode.com/problems/smallest-range/
"""
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.

"""


class Solution:
    def smallestRange(self, A):
        import functools
        A = [row[::-1] for row in A]

        ans = -1e9, 1e9
        for left in sorted(functools.reduce(set.union, map(set, A))):
            right = -1e9
            for B in A:
                while B and B[-1] < left:
                    B.pop()
                if not B:
                    return ans
                right = max(right, B[-1])
            if right - left < ans[1] - ans[0]:
                ans = left, right
        return ans


import heapq
class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        queue = [(list_num[0], i, 0) for i, list_num in enumerate(nums)]
        heapq.heapify(queue)

        result = [float("-inf"), float("inf")]
        right = max(row[0] for row in nums)
        while queue:
            left, i, j = heapq.heappop(queue)
            if right - left < result[1] - result[0]:
                result = [left, right]
            if j == len(nums[i]) - 1:
                return result
            next_num_val = nums[i][j + 1]
            right = max(right, next_num_val)
            heapq.heappush(queue, (next_num_val, i, j + 1))