# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 1 递归
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        elif root.left==None and root.right==None:
            if sum==root.val:
                return True
            else:
                return False
        else:
            return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
    # 2 非递归 使用stack
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """ 
        if root is None:
            return False
        stack = [(root, sum)]
        while stack:
            node, _sum = stack.pop()
            if node.left is node.right is None and node.val == _sum:
                return True
            if node.left:
                stack.append((node.left, _sum - node.val))
            if node.right:
                stack.append((node.right, _sum - node.val))
        return False
