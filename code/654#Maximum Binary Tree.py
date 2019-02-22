# https://leetcode.com/problems/maximum-binary-tree/
"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""
"""
解决方法：
使用递归
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        return self.construct(nums, 0, len(nums))

    def construct(self, nums, l, r):
        if l == r:
            return None
        max_i = nums.index(max(nums[l:r]))
        root = TreeNode(nums[max_i])
        root.left = self.construct(nums, l, max_i)
        root.right = self.construct(nums, max_i+1, r)
        return root


class Solution2:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        q = []

        for c in nums:
            new_node = TreeNode(c)
            while q and q[-1].val < c:
                new_node.left = q.pop()
            if q:
                q[-1].right = new_node
            q.append(new_node)
        print(q)
        return q[0]
