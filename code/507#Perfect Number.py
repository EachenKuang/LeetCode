# https://leetcode.com/problems/perfect-number/description/
class Solution:
    # 1 暴力破解
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in (6,28,496,8128,33550336)
    # 2 常规法
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        res = 1
        bound = int(num**0.5)
        i = 2
        while i <= bound:
            if num%i==0:
                res += i + num//i
                bound = min(bound,num//i)
            if res>num:
                return False
            i+=1
        if res==num:
            return True
        return False



