# https://leetcode.com/problems/first-bad-version/description/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 实际上，这是一个特殊的二分查询
# 一个数的状态只有0,1两种情况，他们按照0,0,0,...,1,1,1,...的顺序排列
# 我们要找到最第一个1。
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分法
        low = 1
        high = n
        while low<high:
            mid = low + (high-low)//2
            if not isBadVersion(mid):
                low = mid+1
            else:
                high = mid
        return high