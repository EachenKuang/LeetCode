# https://leetcode.com/problems/increasing-order-search-tree/
"""
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

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
            \
             7
              \
               8
                \
                 9
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1 递归
class Solution1:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def inorder(node, ans):
            if not node:
                return
            inorder(node.left, ans)
            ans.append(node.val)
            inorder(node.right, ans)

        vals = []
        inorder(root, vals)
        cur = res = TreeNode(0)
        for v in vals:
            cur.right = TreeNode(v)
            cur = cur.right
        return res.right

class Solution2:
    def increasingBST(self, root, tail = None):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res