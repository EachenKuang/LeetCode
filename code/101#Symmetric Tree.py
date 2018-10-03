# https://leetcode.com/problems/symmetric-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 方法一：分层读取，使用队列
        # 方法二：递归
        return self.isMirror(root,root)
    def isMirror(self,node1,node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        else:
            if node1.val == node2.val:
                return self.isMirror(node1.left,node2.right) and self.isMirror(node1.right,node2.left)
            else:
                return False
        