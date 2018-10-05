# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 1 递归，特别需要注意，在计算叶子节点时与maxDepth的区别 
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if not root.left:
            return self.minDepth(root.right)+1
        elif not root.right:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
        # DFS
        def minDepth1(self, root):
            if not root:
                return 0
            if None in [root.left, root.right]:
                return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # BFS   
        def minDepth(self, root):
            if not root:
                return 0
            queue = collections.deque([(root, 1)])
            while queue:
                node, level = queue.popleft()
                if node:
                    if not node.left and not node.right:
                        return level
                    else:
                        queue.append((node.left, level+1))
                        queue.append((node.right, level+1))
