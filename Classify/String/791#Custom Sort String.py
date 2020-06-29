# https://leetcode.com/problems/custom-sort-string/description/
from collections import Counter
class Solution:
    # 1 
    # beat 100%
    # 1、使用collections.Counter()  将字符串返回成计数字典
    # 2、字典的keys()可以直接使用set操作
    # 3、最后结果由join连接所有小片段，减少内存使用
    # 4、生成器比List快
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        c = Counter(T)
        lefted = c.keys()-set(S)        
        return ''.join(letter*c[letter] for letter in ([s for s in S]+[l for l in lefted]))
            