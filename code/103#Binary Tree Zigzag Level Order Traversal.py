# 103. Binary Tree Zigzag Level Order Traversal
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []

        res, level, count = [], [root], 0

        while level:
            res.append([node.val for node in level]) if count % 2 == 0 else res.append(
                [node.val for node in level[::-1]])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [newnode for newnode in temp if newnode]
            count += 1
        return res
