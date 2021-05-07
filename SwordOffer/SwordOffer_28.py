# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
# 例如，二叉树[1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# 但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
# 进阶：
#
# 你可以运用递归和迭代两种方法解决这个问题吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/symmetric-tree
from SwordOffer.DataStruct import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        思路一，用上一题中的翻转算法，先生成一个新的树，然后比较两者是否完全一致
        """
        pass

    def isSymmetric_2(self, root: TreeNode) -> bool:
        """
        递归法
        """
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2 or node1.val != node2.val:
                return False
            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        return isMirror(root, root)

    def isSymmetric_2(self, root: TreeNode) -> bool:
        """
        分层法，先将树转化为分层的数组，然后比较每个数组是否对称
        """
        if not root: return True
        que = [root]
        len_que = len(que)
        while que:
            temp = []
            for _ in range(len_que):
                node = que.pop(0)
                if node:
                    temp.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
                else:
                    temp.append(None)
            if temp != temp[::-1]:
                return False
            len_que = len(que)
        return True




