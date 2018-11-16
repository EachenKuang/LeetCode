# https://leetcode.com/problems/complex-number-multiplication/description/
class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # a_real = int(a[:a.find('+')])
        # a_ima = int(a[a.find('+')+1:-1])
        # b_real = int(b[:b.find('+')])
        # b_ima = int(b[b.find('+')+1:-1])
        res_real = a_real*b_real-a_ima*b_ima
        res_ima = a_real*b_ima+a_ima*b_real
        a_real, a_ima = list(map(int,a[:-1].split('+')))
        b_real, b_ima = list(map(int,b[:-1].split('+')))
        res_real = a_real*b_real-a_ima*b_ima
        res_ima = a_real*b_ima+a_ima*b_real
        
        return "{0}+{1}i".format(res_real, res_ima)