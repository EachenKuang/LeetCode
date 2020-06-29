# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""
2:"abc"
3:"def"
4:"ghi"
5:"jkl"
6:"mno"
7:"pqrs"
8:"tuv"
9:"wxyz"
"""
from itertools import product
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2':"abc",
			'3':"def",
			'4':"ghi",
			'5':"jkl",
			'6':"mno",
			'7':"pqrs",
			'8':"tuv",
			'9':"wxyz"}
        if not digits:
            return []
        return [''.join(combination) for combination in product(*(mapping[i] for i in digits),repeat=1)]
    """
    product(*iterables, repeat=1) --> product object
    For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
    The leftmost iterators are in the outermost for-loop, so the output tuples
    cycle in a manner similar to an odometer (with the rightmost element changing
    on every iteration).
    """
