# https://leetcode.com/problems/binary-tree-paths/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 1 递归
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def searchBT(root,path,ans):
            if root.left==None and root.right==None:
                ans.append(path+str(root.val))
            if root.left:
                searchBT(root.left, path + str(root.val) + "->", ans)
            if root.right:
                searchBT(root.right, path + str(root.val) + "->", ans)
        ans = []
        if root:
            searchBT(root, "", ans)
        return ans
    # 2 使用栈来存储value，然后使用join函数来链接各个value
    def binaryTreePaths(self, r):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = []
        res = []
        def dfs(root):
            if not root:
                return []
            stack.append(root.val)
            if not root.left and not root.right:
                res.append('->'.join(str(v) for v in stack))
            dfs(root.left)
            dfs(root.right)
            stack.pop()
        dfs(r)
        return res
        