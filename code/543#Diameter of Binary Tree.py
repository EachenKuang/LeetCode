# https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxD = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """       
        def maxDepth(root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.maxD = max(self.maxD, left + right)
            return max(left, right) + 1
        self.maxD = 0 
        maxDepth(root)
        return self.maxD
        