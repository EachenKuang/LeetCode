# https://leetcode.com/problems/binary-gap/
"""
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.



Example 1:

Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation:
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation:
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation:
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.


Note:

1 <= N <= 10^9
"""


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        temp = bin(N)
        if temp.count('1') <= 1:
            return 0
        return len(max(bin(N)[2:].split('1')[1:-1], key=len)) + 1


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max = 0
        str = bin(N)[2:]
        lst = []

        for i in range(len(str)):
            if int(str[i]) == 1:
                lst.append(i)

        if len(lst) < 2: return 0

        for i in range(len(lst)):
            if max < lst[i] - lst[i - 1]:
                max = lst[i] - lst[i - 1]

        return max

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = str(bin(N))
        count = 0
        last = n.index('1')
        for i in range(last+1, len(n)):
            if n[i] =='1':
                if count < i - last:
                    count = i - last
                last = i
        return count