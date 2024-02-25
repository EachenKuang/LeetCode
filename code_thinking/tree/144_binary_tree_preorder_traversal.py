# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 9:07
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 144_binary_tree_preorder_traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from code_thinking.data_struct import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """递归 recursion"""
        if root is None:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """迭代 iteration"""
        result = []
        if not root:
            return []
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            # 注意先添加右子树
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result
