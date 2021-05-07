# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
from SwordOffer.DataStruct import TreeNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """
        递归
        时间复杂度：O(n)
        空间复杂度：O(n) 最差的情况下，二叉树为链表结构，需要暂存左节点，而Python可以平行赋值，可省略
        """
        if not root:
            return root
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

    def mirrorTree_2(self, root: TreeNode) -> TreeNode:
        """
        非递归，使用辅助栈
        时间复杂度：O(n)
        空间复杂度：O(n) 最差的情况下，二叉树为链表结构，需要存一半的节点
        """
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root

