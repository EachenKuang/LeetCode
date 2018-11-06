# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
	# 1 BFS
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        q, level = root and [root], 0
        while q:
            q, level = [child for node in q for child in node.children if child], level + 1
        return level 
    # 2 DFS
    def maxDepth(self, root, level = 1):
        return max(root and [self.maxDepth(child, level + 1) for child in root.children] + [level] or [0])