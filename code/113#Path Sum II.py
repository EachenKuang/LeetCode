# https://leetcode.com/problems/path-sum-ii/
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
        return res

    def pathSum(self, root, s):
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res