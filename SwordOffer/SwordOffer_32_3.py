# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
#  
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#
# 提示：
#
# 节点总数 <= 1000
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
from typing import List
from SwordOffer.DataStruct import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """

        """
        from collections import deque
        if not root:
            return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            tmp = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(tmp))
        return res