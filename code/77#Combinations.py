# https://leetcode.com/problems/combinations/
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution1:
    def combine(self, n: int, k: int) -> list[list[int]]:
        from itertools import combinations
        return list(combinations(range(1,n+1),k))

    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':

        res = []
        cur_res = [None] * k

        def dfs(i=0, j=0):
            # print(i,j)
            for j in range(j, n):
                cur_res[i] = j + 1
                if i == k - 1:
                    res.append(cur_res[:])
                else:
                    dfs(i + 1, j + 1)

        dfs()
        return res

    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        # print(n, k)
        if k > n:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]
        res = self.combine(n - 1, k)
        # print(res)
        part = self.combine(n - 1, k - 1)
        # print(part)
        for p in part:
            res.append(p + [n])
        return res

    def combine(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1