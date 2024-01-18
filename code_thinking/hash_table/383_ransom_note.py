# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 22:00
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 383_ransom_note.py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        字典法
        1.先将杂志上
        """
        res = dict()
        for i in magazine:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        for j in ransomNote:
            if j not in res:
                return False
            res[j] -= 1
            if res[j] < 0:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        """
        数组法
        因为只有小写字母，使用一个 26长度的数组进行计数也可实现
        """
        record = [0] * 26
        for i in magazine:
            record[ord(i) - ord('a')] += 1

        for j in ransomNote:
            record[ord(j) - ord('a')] -= 1
            if record[ord(j) - ord('a')] < 0:
                return False
        return True


