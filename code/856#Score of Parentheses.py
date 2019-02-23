# https://leetcode.com/problems/score-of-parentheses/description/
class Solution:
    # 1
    # one line cheat
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        return eval(S.replace(')(', ')+(').replace('()', '1').replace(')', ')*2'))        power = 0
        ans = 0
    # 2 
    # 只有两种情况
    # 1)   ((()))   
    # 2)   ()()
    def scoreOfParentheses(self, S):

        for letter in S:
            
            if letter == '(':
                power += 1
                sig = 1
                continue
            
            if letter == ')':
                power -= 1
                if sig:
                    ans += 2**power
                sig = 0
                
        return ans
    # 3 
    def scoreOfParentheses(self, s):
        res = layers = 0
        for a, b in itertools.izip(S, S[1:]):
            layers += 1 if a == '(' else -1
            if a + b == '()': res += 2 ** (layers - 1)
        return res