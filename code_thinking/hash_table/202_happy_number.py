# -*- coding: utf-8 -*-
# @Time    : 2024/1/16 23:39
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 202_happy_number.py
class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()  # 用来记录循环
        while True:
            n = self.calculate(n)
            if n == 1:
                return True
            if n in memo:
                return False
            else:
                memo.add(n)

    def calculate(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n % 10) * (n % 10)
            n = n // 10
        return res

    def isHappy2(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            new_num = 0
            n_str = str(n)
            for i in n_str:
                new_num += int(i) ** 2
            if new_num == 1:
                return True
            else:
                n = new_num
        return False
