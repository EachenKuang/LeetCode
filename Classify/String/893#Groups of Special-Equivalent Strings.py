# https://leetcode.com/problems/groups-of-special-equivalent-strings/description/
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        B = set()
        for s in A:
            a, b = s[::2], s[1::2]
            B.add((''.join(sorted(a)), ''.join(sorted(b))))
            
        return len(B)