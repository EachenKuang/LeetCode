# https://leetcode.com/problems/reordered-power-of-2/
"""
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9
"""


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        pow_of_2 = {'1',
                     '2',
                     '4',
                     '8',
                     '16',
                     '23',
                     '46',
                     '128',
                     '256',
                     '125',
                     '0124',
                     '0248',
                     '0469',
                     '1289',
                     '13468',
                     '23678',
                     '35566',
                     '011237',
                     '122446',
                     '224588',
                     '0145678',
                     '0122579',
                     '0134449',
                     '0368888',
                     '11266777',
                     '23334455',
                     '01466788',
                     '112234778',
                     '234455668',
                     '012356789'}
        return ''.join(sorted(str(N))) in pow_of_2


class Solution2:
    powers = {''.join(sorted(str(1 << x))) for x in range(31)}

    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return ''.join(sorted(str(N))) in Solution.powers
