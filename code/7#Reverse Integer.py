# https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)

        if x >= 0 and int(str_x[::-1]) <= (2**31-1):
            return int(str_x[::-1])
        elif x < 0 and -int(str_x[:0:-1]) >= (-2**31):
            return -int(str_x[:0:-1])
        else:
            return 0
