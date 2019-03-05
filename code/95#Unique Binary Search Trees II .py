# https://leetcode.com/problems/unique-binary-search-trees-ii/
"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        def generate(first, last):
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            return trees or [None]
        return generate(1, n)
        
class Solution:
    
    memo = {}
    
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        if (n == 0):
            return []
        return self.treesInRange(1, n)
    
    def treesInRange(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i > j:
            return [None] #Need a placeholder for the all pairs iter below
        if i == j:
            return [TreeNode(i)]
        sols = []
        for v in range(i, j + 1):
            lessThan = self.treesInRange(i, v - 1)
            greaterThan = self.treesInRange(v + 1, j)
            # All combos of this root with left and right subtrees
            withRoot = []
            for lt in lessThan:
                for rt in greaterThan:
                    root = TreeNode(v)
                    root.left = lt
                    root.right = rt
                    withRoot.append(root)
            sols.extend(withRoot)
        self.memo[(i, j)] = sols
        return sols