# https://leetcode.com/problems/merge-two-binary-trees/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# 1 递归 构造新的树
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
	    if not t1 and not t2: 
	    	return None
	    ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
	    ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
	    ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
	    return ans
	# 2 递归 在原树的基础上构造
	def mergeTrees(self, t1, t2):
		if t1 and t2:
			t1.val += t2.val
			t1.left = self.mergeTrees(t1.left,t2.left)
			t2.right = self.mergeTrees(t1.right,t2.right)
			return t1
		else:
			return t1 or t2	
	# 3 使用栈非递归
	# 按顺序存入栈

