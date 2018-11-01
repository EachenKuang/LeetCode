# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1 insorder find 
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.mode = set()
        self.max_freq = 0
        self.cur_freq = 0
        self.cur_item = None
        if root:
            self.inorder(root)
        return list(self.mode)
    
    def calc_freq(self, value):
        if self.cur_item == value:
            self.cur_freq += 1
        else:
            self.cur_item = value
            self.cur_freq = 1
        if self.max_freq < self.cur_freq:
            self.mode = set([self.cur_item])
            self.max_freq = self.cur_freq
        elif self.max_freq == self.cur_freq:
            self.mode.append(self.cur_item)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.calc_freq(root.val)
            self.inorder(root.right)
# 2 using stack to store the value inoder
class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        pre, cur, stack, cur_count, max_count, modes = None, root, [], 0, 0, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not pre or cur.val == pre.val:  # same as previous value, increase frequence by 1
                cur_count += 1
            else:                              # different value from pre, update modes and reset current frequency
                if cur_count > max_count:
                    max_count = cur_count
                    modes = [pre.val]
                elif cur_count == max_count:
                    modes.append(pre.val)
                cur_count = 1
            pre = cur
            cur = cur.right
        if cur_count > max_count:  # handle last value
            return [pre.val]
        elif cur_count == max_count:
            modes.append(pre.val)
        return modes