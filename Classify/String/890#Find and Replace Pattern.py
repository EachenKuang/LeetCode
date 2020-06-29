# https://leetcode.com/problems/find-and-replace-pattern/description/

# 这个题目与之前的 205#Isomorphic Strings.py 是同样的道理
# 可以参照这个文档中的函数is_isomorohic
class Solution:
    # filter(function, iter)过滤出符合条件的成员，返回list
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        patter_list = [pattern.find(i) for i in pattern]
        def is_iso(word):
            return [word.find(j) for j in word]==patter_list
        return list(filter(is_iso,words))