# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        val = postorder.pop()
        root = TreeNode(val)
        i = inorder.index(val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:])
        return root

class Solution2
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:       
        if len(postorder) == 0:
            return []
        
        flag = False
        root = None
        stack = []
        postorder = postorder[::-1]
        for i in range(len(postorder)):
            new_node = TreeNode(postorder[i])
            if not root:
                root = new_node
            else:
                if not flag:
                    node.right = new_node
                else:
                    node.left = new_node
                    flag = False
            stack.append(new_node)
            node = stack[-1]
            while stack and stack[-1].val == inorder[-1]:
                node = stack.pop()
                inorder.pop()
                flag = True
        return root