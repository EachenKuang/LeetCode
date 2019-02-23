# https://leetcode.com/problems/valid-triangle-number/description/
"""
Given an array consists of non-negative integers,
your task is to count the number of triplets
chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].

"""
# 1
# 先找出组合
from itertools import combinations
class Solution1:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_triangle(*args):
            a, b, c= args
            if a + b > c > 0 and a + c > b > 0 and b + c > a > 0:
                return 1
            return 0
        return sum([is_triangle(*com) for com in combinations(nums, 3)])

# 2
# 先排序再计算
class Solution2:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(2, len(nums)):
            l,r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r-l
                    r -= 1
                else:
                    l += 1
        return count

if __name__ == '__main__':
    t = Solution1()
    print(t.triangleNumber([2,2,3,4]))
