# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution:
    # 1 最先想到的一种解法，但是TLE（Time Limit Exceeded）
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1
    # 2 
    # 改进，先将count为1的字符保存下来
    # 然后使用index找到标号最前的
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        ret = len(s)
        for i in set(s):
            if s.count(i)==1:
                res.append(i)
        if not res:
            return -1
        for i in res:
            ret = min(ret,s.index(i))
        return ret

    # 3
    # 使用find和rfind，利用双向链表的特性查找
    # 字符限制在有效的以内
    def firstUniqChar(self, s):

        if not s: return -1
        L = len(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            left = s.find(c)
            right = s.rfind(c)
            if 0<=left<L and left==right:
                L = left
        return L if L<len(s) else -1