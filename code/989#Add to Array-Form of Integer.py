# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        
        def inorder(root: 'TreeNode', temp_list: []):
            if not root:
                return
            inorder(root.left, temp_list)
            temp_list.append(root.val)
            inorder(root.right, temp_list)
        
        tree_list = []
        inorder(root, tree_list)
        l = 0
        r = len(tree_list)-1
        while l < r:
            sum = tree_list[l] + tree_list[r]
            if sum == k:
                return True
            if sum < k:
                l += 1
            else:
                r -= 1
        return False

class Solution2:            
    def findTarget(self, root, k):
            if not root: return False
            bfs, s = [root], set()
            for i in bfs:
                if k - i.val in s: return True
                s.add(i.val)
                if i.left: bfs.append(i.left)
                if i.right: bfs.append(i.right)
            return False