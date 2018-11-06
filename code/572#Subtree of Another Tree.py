# https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, a, b):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not b:
            return True
        
        def checkTree(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2 or root2 and not root1:
                return False
            
            if root1.val != root2.val:
                return False
            
            return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)
        
        def dfs(s, t):
            if not s:
                return False
            
            if s.val == t.val and checkTree(s, t):
                return True
            
            return dfs(s.left, t) or dfs(s.right, t)
            
        return dfs(a, b)