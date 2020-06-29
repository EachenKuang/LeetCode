# https://leetcode.com/problems/top-k-frequent-elements/description/
"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter


class Solution:
    # 1
    # one line
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [v for v, c in Counter(nums).most_common(k)]
        # mapping = Counter(nums).most_common(k)
        # return [v for v,c in mapping]
    # 2
    # 使用堆heapq
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1

        lst = []
        for e in m:
            heapq.heappush(lst, (-m[e], e))
        res = []
        for i in range(k):
            res.append(heapq.heappop(lst)[1])
        return res

if __name__ == '__main__':
    t = Solution()
    print(t.topKFrequent([1,1,1,2,2,3,4],2))