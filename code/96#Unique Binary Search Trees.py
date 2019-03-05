# https://leetcode.com/problems/unique-binary-search-trees/
"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution:
    def numTrees(self, n: 'int') -> 'int':
        count = 0
        d = {0: 1, 1: 1}
        for i in range(2, n + 1):
            total = 0
            for j in range(i):
                total += d[j] * d[i - j - 1]             
            d[i] = total           
        return d[n]
    # DP
	def numTrees1(self, n):
	    res = [0] * (n+1)
	    res[0] = 1
	    for i in xrange(1, n+1):
	        for j in xrange(i):
	            res[i] += res[j] * res[i-1-j]
	    return res[n]
	 
	# Catalan Number  (2n)!/((n+1)!*n!)  
	def numTrees(self, n):
	    return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))