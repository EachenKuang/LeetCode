# https://leetcode.com/problems/base-7/description/
class Solution:
    # 1 常规方法
    # 需要区分正负数与零
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = 0
        if num == 0:
            return "0"
        elif num < 0:
            flag = 1
            num = 0-num
        res = []
        while num:
            bit = num%7
            num = num//7
            res.insert(0,str(bit))
        return ''.join(res) if flag==0 else "-"+''.join(res)