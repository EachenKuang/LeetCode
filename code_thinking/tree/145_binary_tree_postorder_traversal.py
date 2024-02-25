# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 9:15
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 145_binary_tree_postorder_traversal.py
from typing import Optional, List

from code_thinking.data_struct import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """递归 recursion"""
        if root is None:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return left + right + [root.val]

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """迭代 iteration"""
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]
