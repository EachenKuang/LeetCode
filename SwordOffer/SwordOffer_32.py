# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
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
# 返回：
#
# [3,9,20,15,7]
#  
#
# 提示：
#
# 节点总数 <= 1000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
from typing import List

from SwordOffer.DataStruct import TreeNode



class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        """
        Python 中使用 collections 中的双端队列 deque() ，其 popleft() 方法可达到 O(1)时间复杂度；
        列表 list 的 pop(0) 方法时间复杂度为 O(N) 。
        """
        from collections import deque
        que = deque()
        if root:
            que.append(root)
        result = []
        while que:
            node = que.popleft()
            result.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return result