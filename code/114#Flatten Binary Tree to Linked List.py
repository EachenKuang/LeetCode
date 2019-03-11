# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        last=TreeNode(-1)
        qstack=[root]
        while qstack:
            node=qstack.pop()
            last.right=node
            last.left=None
            if node and node.right:
                qstack.append(node.right)
            if node and node.left:
                qstack.append(node.left)
            last=node