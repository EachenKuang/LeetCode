# https://leetcode.com/problems/find-the-difference/description/
class Solution:
    # 1 （错误）
    # 一开始误以为添加的字母是另一个，但是测试时发现还可能是"a"与 "aa"的情况
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return (set(t)-set(s)).pop()
    # 2  66.94%
    # 因为题目只包含小写字母，所以循环遍历小写字母
    # 找到count不同的字母，答案就是了。
    # O(n)
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(c)!=t.count(c):
                return c
    # 3 100%
    # 使用内部类Count 个人不推荐
    from collections import Counter
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_count, t_count = Counter(s), Counter(t)
        for k, v in t_count.items():
            if k not in s_count:
                return k
            if v > s_count[k]:
                return k
    # 4 99%
    # 因为两个字符串就相差一个字符，那么将两个字符串的ASCLL码的和相减
    # 即可得到对应的字符的ASCLL码，然后使用ord与chr转化即可
    # 这个题真是巧妙
    def findTheDifference(self, s, t):
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)
    # 5 使用xor
    def findTheDifference(self, s, t):
        xr = 0
        for c in s:
            xr = xr ^ ord(c)
        for c in t:
            xr = xr ^ ord(c)
        return chr(xr)