# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 9:17
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 94_binary_tree_inorder_traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from code_thinking.data_struct import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        递归法 recursion
        """
        if root is None:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """
        迭代法 iteration
        """
        result = []
        stack = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:
                stack.append(cur)  # 左
                cur = cur.left
            # 到达最左结点后处理栈顶结点
            else:
                cur = stack.pop()
                result.append(cur.val)  # 中
                # 取栈顶元素右结点
                cur = cur.right  # 右
        return result
