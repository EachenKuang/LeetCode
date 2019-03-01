# https://leetcode.com/problems/gray-code/
"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
Therefore, for n = 0 the gray code sequence is [0].
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        j = 0
        while n > 0:      
            ans.extend(i + 2**j for i in reversed(ans))
            j += 1
            n -= 1
        return ans
# Runtime: 40 ms, faster than 54.98% of Python3 online submissions for Gray Code.
# Memory Usage: 13.1 MB, less than 13.63% of Python3 online submissions for Gray Code.       
class Solution:
    def grayCode(self, n: 'int') -> 'List[int]':
        if n==0: return [0]
        if n<0: return []
        
        res = [0]
        for i in range(n):
            add = 1<<i
            tmp = []
            for i in reversed(res):
                tmp.append(i^add)
            res.extend(tmp)
        return res