# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1 使用递归
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0
        def visit(root):
            if root:
                visit(root.right)
                root.val += self.val
                self.val = root.val
                visit(root.left)
        visit(root)
        return root

# 2 非递归
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        stack = [root]
        node = root.right
        sumVal = 0
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            sumVal += node.val
            node.val = sumVal
            
            node = node.left
            
        return root