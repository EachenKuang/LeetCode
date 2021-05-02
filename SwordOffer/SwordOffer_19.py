# 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        动态规划的题目，需要找到状态转移方程
        定义一个数组dp[m+1][n+1]来保存对应的状态
        定义：dp[i][j]表示 s[:i] 与 p[:j]能否匹配
        总体思路是从 s[:1] 和 p[:1]是否能匹配开始判断，每轮添加一个字符并判断是否能匹配，直至添加完整个字符串 s 和 p 。
        展开来看，假设 s[:i] 与 p[:j]可以匹配，那么下一状态有两种：
        添加一个字符 s_{i+1}后是否能匹配？
        添加字符 p_{j+1}后是否能匹配？


        """
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') \
                           if p[j - 1] == '*' else \
                           dp[i - 1][j - 1] and (p[j - 1] == '.' or s[i - 1] == p[j - 1])
        return dp[-1][-1]
