# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # 找各个数的最大公约数，当最大公约数大于或等于2，则True
        from collections import Counter
        from functools import reduce
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return a
        count = Counter(deck).values()
        return reduce(gcd,count)>=2

    def hasGroupsSizeX(self, deck):
        return reduce(fractions.gcd, collections.Counter(deck).values()) > 1
        
