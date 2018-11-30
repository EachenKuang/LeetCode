# https://leetcode.com/problems/to-lower-case/description/
class Solution:
    # 1 使用内置函数lower()
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
    # 2 对于A~Z的字符进行转换 Ascll码+32
    def toLowerCase2(self, str):
        result = ""
        for c in str:
            if c >="A" and c<="Z":
                result= result+chr(ord(c)+32)
            else:
                result =result+ c
        return result