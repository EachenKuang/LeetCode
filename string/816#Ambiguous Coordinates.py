# https://leetcode.com/problems/ambiguous-coordinates/description/
class Solution(object):
    # 1
    # 策略
    # 第一步：先加逗号，将数分成两部分
    # 第二步：对每部分加点号
    # 第三步：剔除不满足的情况
    def ambiguousCoordinates(self, S):
        S = S[1:-1]
        def f(S):
            if not S or len(S) > 1 and S[0] == S[-1] == '0': return []
            if S[-1] == '0': return [S]
            if S[0] == '0': return [S[0] + '.' + S[1:]]
            return [S] + [S[:i] + '.' + S[i:] for i in range(1, len(S))]
        return ['(%s, %s)' % (a, b) for i in range(len(S)) for a, b in itertools.product(f(S[:i]), f(S[i:]))]
        
class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]
        res = []
        for i in range(1, len(S)):
            left = self.point(S[:i])
            right = self.point(S[i:])
            
            for l in left:
                for r in right:
                    res.append("(" + l + ", " + r + ')')
                    
        return res

    def point(self, s):
        if s[0] == '0' and s[-1] == '0': return ['0'] if s == '0' else []
        if s[-1] == '0': return [s]
        if s[0] == '0': return [s[0] + '.' + s[1:]]

        return [s[:i] + '.' + s[i:] for i in range(1, len(s))] + [s]