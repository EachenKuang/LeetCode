# https://leetcode.com/problems/combination-sum-iii/
"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
# 利用内置函数 100%
class Solution1:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        return [com for com in combinations(range(1,10),k) if sum(com) == n]

# 之前的100%解答
class Solution2:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        re = []

        def dfs(curr, target):
            if len(re) == k:
                if target == 0:
                    res.append(list(re))
                return
            if curr == 10:
                return
            for i in range(curr, 10):
                if target - i < 0:
                    break
                re.append(i)
                dfs(i + 1, target - i)
                re.remove(i)

        dfs(1, n)

        return res
if __name__ == '__main__':
    t = Solution1()
    print(t.combinationSum3(3,9))
    print(t.combinationSum3(3,100))
    print(t.combinationSum3(0,9))