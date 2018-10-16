# https://leetcode.com/problems/add-digits/description/
# Could you do it without any loop/recursion in O(1) runtime?
class Solution:
    # 1 常规方法
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            result=0
            while num !=0:
                ind = num % 10
                num = num // 10
                result += ind
            if result<10:
                break
            else:
                num=result
        return result
    # 2 使用python特性map three line
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            num = sum(map(int,str(num)))
        return num
    # 3 使用数论的技巧
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: 
            return 0
        else:
            return (num - 1) % 9 + 1