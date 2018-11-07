# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# 1 非递归
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = []
        res = []
        
        stack.append(root)
        
        while len(stack) > 0:
            curr = stack.pop()
            if curr.children is not None:
                stack.extend(curr.children)
            res.append(curr.val)

# 2 递归
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        lst = [root.val]
        for node in root.children[::-1]:
            lst = self.postorder(node) + lst
        return lst