# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# 1 使用stack的非递归方法
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        stack = [root]
        
        while len(stack) != 0:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(reversed(cur.children))
        return result
# 2 递归法
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        lst = [root.val]
        for node in root.children:
            lst += self.preorder(node)
        return lst
