# https://leetcode.com/problems/balanced-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 1 使用104中的maxDepth
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 1 用递归
        if root == None:
            return True;
        flag =  abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1
        return flag and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    # 2 一个函数递归
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 1 用递归
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return dfs(root) != -1
        
