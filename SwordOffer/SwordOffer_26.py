# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# 
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
# 
# 例如:
# 给定的树 A:
# 
#         3
#       / \
#      4    5
#    / \
#   1    2
# 给定的树 B：
# 
#      4  
#    /
#   1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
from SwordOffer.DataStruct import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        递归方法
        """
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
