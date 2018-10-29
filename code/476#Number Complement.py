class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 1 
        # 先计算出位数l
        # 取反的数与原数相加为1后面l个0
        # 5：101    2：010   5+2=7:111
        s = bin(num)[2:]
        l = len(s)
        return 2**l-1-num