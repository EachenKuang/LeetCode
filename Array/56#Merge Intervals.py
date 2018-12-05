# https://leetcode.com/problems/insert-interval/description/
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
# 1
# 题目预设是排好序的intervals，且没有重叠
# 那么只需找到新的interval在intervals的位置即可

class Solution:

    # 1
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        res = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                res.append(intervals[i])
            i += 1
        res.append(Interval(start, end))
        res += intervals[i:]
        return res

    # 2
    def insert2(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s,e = newInterval.start, newInterval.end
        left = [inter for inter in intervals if inter.end<s]
        right = [inter for inter in intervals if inter.start>e]
        if len(left) + len(right)<len(intervals):
            start = min(intervals[len(left)].start, s)
            end = max(intervals[-len(right)-1].end, e)
            newInterval = Interval(start, end)
        return left + [newInterval] + right