# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """       
        if not root:
            return []
        res = []
        lis = [root]
        while lis:
            lis2 = []
            level_sum = 0
            for each in lis:
                level_sum += each.val
                if each.left:
                    lis2.append(each.left)
                if each.right:
                    lis2.append(each.right)

            res.append(level_sum / len(lis))
            lis = lis2
        return res
        