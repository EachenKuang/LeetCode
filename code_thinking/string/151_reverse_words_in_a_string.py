# -*- coding: utf-8 -*-
# @Time    : 2024/1/20 11:28
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 151_reverse_words_in_a_string.py
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def reverseWords2(self, s: str) -> str:
        s = s.split()

        start = 0
        end = len(s) - 1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return ' '.join(s)

    def reverseWords3(self, s: str) -> str:
        res = []
        temp = []
        for i in s:
            if i == " ":
                if temp:
                    res.append("".join(temp))
                    temp = []
            else:
                temp.append(i)
        # 处理最后没有空格的情况
        if temp:
            res.append("".join(temp))
        return ' '.join(res[::-1])


if __name__ == '__main__':
    input_list = [
        # "blue sky in my e",
        "  hello world  "
    ]
    solution = Solution()
    for s in input_list:
        print(solution.reverseWords3(s))


