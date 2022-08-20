
# https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/
# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 切片法
        return s[n:] + s[:n]

    def reverseLeftWords(self, s: str, n: int) -> str:
        # 三次翻转
        # 先翻转0:n,然后翻转n:-1,最后整个数组翻转

        pass
