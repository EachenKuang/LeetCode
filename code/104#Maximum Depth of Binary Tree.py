# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# 1 递归方法
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    # 2 使用非递归
    def maxDepth(self, root):
        stack = [(root, 1)]
        total = 0
        while stack:
            node, depth = stack.pop()
            if node:
                total = max(total, depth)
                stack.extend([(node.left, depth + 1), (node.right, depth + 1)])
        return total