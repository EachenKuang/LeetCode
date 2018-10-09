# https://leetcode.com/problems/excel-sheet-column-title/description/
class Solution:
    # 1 直接使用字母表
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while n > 0:
            word = (n-1) % 26
            n = (n-1) // 26
            tempString = alpha[word]
            res = ''.join((tempString, res))            
        return res
    # 2 利用chr与ord函数
    # chr(65)='A';ord('A')=65
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        dist = ord('A') 

        while n > 0:
            word = (n-1) % 26
            n = (n-1) // 26
            tempString = chr(word+dist)
            res = ''.join((tempString, res))            
        return res