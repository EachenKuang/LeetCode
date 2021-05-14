# 请实现两个函数，分别用来序列化和反序列化二叉树。
#
# 示例: 
#
# 你可以将以下二叉树：
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
from SwordOffer.DataStruct import TreeNode
from collections import deque

class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'


    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return
        values = data[1:-1].split(',')
        root = TreeNode(int(values[0]))
        queue = deque()
        queue.append(root)
        i = 1
        while queue:
            node = queue.popleft()
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root
