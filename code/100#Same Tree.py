# https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 1 递归
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
    # 2 非递归 通过堆栈
    # 直接将树转化为队列，有可能会出现序列一致但是树不同的情况
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def traverse(root):
            queue=[root]
            res=[]
            while queue:
                temp = queue.pop(0)
                if temp:
                    res.append(temp.val)

                    queue.append(temp.left)

                    queue.append(temp.right)
                    
                else:
                    res.append(None)
                
            
            return res
        
        lista = traverse(p)
        listb = traverse(q)
        
        return lista==listb