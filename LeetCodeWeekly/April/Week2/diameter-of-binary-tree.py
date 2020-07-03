# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
from LeetCodeWeekly.meta_class import TreeNode

# 使用递归
# 根节点，
class Solution:
    maxD = 0
    def diameterOfBinaryTree(self, root):

        def maxDepth(root):
            if root is None:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.maxD = max(self.maxD, left + right)
            return max(left, right) + 1
        self.maxD = 0
        maxDepth(root)
        return self.maxD


class Solution1:
    def maxLength(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = [(root, 1)]
        longest = 1

        while q:
            node, level = q.pop(0)
            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))
            longest = level if level > longest else longest
        # print(longest)
        return longest

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 0

        longest = 0

        q = [root]

        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            max_path = self.maxLength(node.left) + self.maxLength(node.right)
            longest = max_path if max_path > longest else longest

        return longest