# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 限制：
#
# 0 <= 节点个数 <= 5000
from typing import List

from SwordOffer.DataStruct import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """递归的方法"""
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        index = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

