https://leetcode.com/problems/reverse-bits/description/
class Solution:
    # @param n, an integer
    # @return an integer
    # 1
    # 需要考虑32位这个点，有可能转化过来的二进制数零
    # 的位数不够32，需要补齐
    # int(str，base) bin(num)函数的使用
    def reverseBits(self, n):  
        s = bin(n)[2:]
        if len(s)<=32:
            s2 = '0b'+s[::-1]+(32-len(s))*'0'
        return int(s2,2)
    # 2
    # 通过移位循环32次，使用n&1返回满足的最低位
    # 法二挺巧妙的
    def reverseBits(self, n):
        res = 0
        for _ in xrange(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res