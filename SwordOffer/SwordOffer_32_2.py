from typing import List

from SwordOffer.DataStruct import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
