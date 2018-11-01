# https://leetcode.com/problems/relative-ranks/description/
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        N = len(nums)
        p = [(n, i) for i, n in enumerate(nums)]
        p = sorted(p, key=lambda x: x[0], reverse=True)
        ans = [0] * N
        for rank in range(N):
            idx = p[rank][1]
            if rank == 0:
                ans[idx] = "Gold Medal"
            elif rank == 1:
                ans[idx] = "Silver Medal"
            elif rank == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank+1)
        return ans