# https://leetcode.com/problems/find-and-replace-in-string/description/
class Solution(object):
    # 1 
    # 反序很关键，可以从右往左遍历使用index
    # 利用zip函数
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        listOfS = list(S)
        distance = 0
        for index,source,target in sorted(zip(indexes, sources, targets),reverse=True):
            if S[i:i + len(s)] == s:
                listOfS[index:index+len(source)]=target
        return "".join(listOfS)
        
    def findReplaceString2(self, S, indexes, sources, targets):        
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
        return S