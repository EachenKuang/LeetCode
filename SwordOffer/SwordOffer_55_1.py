# https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from SwordOffer.DataStruct import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 使用递归
        ans = 0
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: TreeNode) -> int:
        # 非递归，需要使用一个队列来保存
        if not root:
            return 0
        queue = [root]
        ans = 0
        cur_level_size = 1
        while queue:
            node = queue.pop()
            cur_level_size -= 1
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
            # 遍历完该层的队列数量，就跳到下一层了
            if cur_level_size == 0:
                cur_level_size = len(queue)
                ans += 1
        return ans


