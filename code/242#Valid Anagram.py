# https://leetcode.com/problems/valid-anagram/description/
class Solution:
    # 1 使用count beat 98%
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 判断含字母的个数是否一致
        if len(set(s))!=len(set(t)):
            return False
        alpha = set(s)
        for i in alpha:
            if s.count(i)!=t.count(i):
                return False
        return True
    # 2 使用字典
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for i in s:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for j in t:
            if j in dic2:
                dic2[j] += 1
            else:
                dic2[j] = 1
        return dic1 == dic2
    # 3 使用 from collections import Counter 不推荐
    from collections import Counter
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_d = Counter(s)
        t_d = Counter(t)
        if len(s_d.keys()) != len(t_d.keys()):
            return False
        
        for key in s_d:
            if s_d[key] != t_d[key]:
                return False
        return True