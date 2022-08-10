# https://leetcode.cn/problems/smallest-string-starting-from-leaf/
# 给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个 [0, 25] 范围内的值，分别代表字母 'a' 到 'z'。
# 返回 按字典序最小 的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

# 注：字符串中任何较短的前缀在 字典序上 都是 较小 的：

# 例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。 
# 节点的叶节点是没有子节点的节点。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from LeetCodeWeekly.meta_class import TreeNode


class Solution:
    def smallestFromLeaf(self, root):
        """
        暴力法，找出所有的路径，通过反转后进行比较
        """
        self.ans = "~"

        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(A)))

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()

        dfs(root, [])
        return self.ans

        
