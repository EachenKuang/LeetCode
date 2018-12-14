# https://leetcode.com/problems/longest-harmonious-subsequence/description/
"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        res = 0
        mapping = Counter(nums)
        for k in mapping.keys():
            if k+1 in mapping:
                res = max(res, mapping.get(k) + mapping.get(k+1))
        return res


