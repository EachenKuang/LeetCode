from typing import List

from SwordOffer.DataStruct import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def recur(root, tar):
            if not root:
                return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res

    def pathSum_2(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []

        res, stack = [], [(root, root.val, [root.val])]
        while stack:
            cur, tmpres, path = stack.pop()
            if tmpres == target and not cur.left and not cur.right:
                res.append(path)
            if cur.left:
                stack.append((cur.left, tmpres + cur.left.val, path + [cur.left.val]))
            if cur.right:
                stack.append((cur.right, tmpres + cur.right.val, path + [cur.right.val]))
        return res
