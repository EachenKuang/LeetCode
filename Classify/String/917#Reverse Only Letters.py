# https://leetcode.com/problems/reverse-only-letters/description/
"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        temp = list(S)
        left = 0
        right = len(temp) - 1
        while left < right:
            while left < right and not temp[left].isalpha():
                left += 1
            while left < right and not temp[right].isalpha():
                right -=1
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1
        return ''.join(temp)