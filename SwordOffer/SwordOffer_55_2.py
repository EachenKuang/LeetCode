# https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from DataStruct import TreeNode, list_to_binary_tree


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        # 使用递归
        ans = 0
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        # 递归法，自顶向下
        if not root:
            return True
        # 计算左右子树的深度是否相差1
        minus = self.maxDepth(root.left) - self.maxDepth(root.right)
        if minus > 1 or minus < -1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, None, None, 5, 6]
    test_list1 = [1,2,2,3,3,None,None,4,4]
    test_list_node = list_to_binary_tree(test_list1)
    solution = Solution()
    print(solution.isBalanced(test_list_node))