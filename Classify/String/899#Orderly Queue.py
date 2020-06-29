# https://leetcode.com/problems/orderly-queue/
"""
A string S of lowercase letters is given.  Then, we may make any number of moves.

In each move, we choose one of the first K letters (starting from the left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.



Example 1:

Input: S = "cba", K = 1
Output: "acb"
Explanation:
In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".
Example 2:

Input: S = "baaca", K = 3
Output: "aaabc"
Explanation:
In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".


Note:

1 <= K <= S.length <= 1000
S consists of lowercase letters only.
"""
# 分析情况：
# 当K=1时，相当于一个环，可以的组合有n种，选取最小的那个组合
# 当K=2时，相当于一个可以移动相邻两个字母的环，这种情况下，实际上可以是任意的组合
# 当K>2时，情况与K=2一样。
class Solution(object):
    def orderlyQueue(self, S, K):
        return "".join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))
        # if K == 1:
        #     return min(S[i:] + S[:i] for i in range(len(S)))
        # return "".join(sorted(S))
