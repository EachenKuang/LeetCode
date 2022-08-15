def LCS(L, S):
    if not L or not S:
        return ""
    res = ''
    dp = [[0] * (len(L) + 1) for i in range(len(S) + 1)]
    flag = [['left'] * (len(L) + 1) for i in range(len(S) + 1)]
    for i in range(len(S) + 1):
        for j in range(len(L) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                flag[i][j] = '0'
            else:
                if L[j - 1] == S[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    flag[i][j] = 'ok'
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    flag[i][j] = 'up' if dp[i][j] == dp[i - 1][j] else 'left'
    return dp[-1][-1], flag


def printres(flag, L, S):
    m = len(flag)
    n = len(flag[0])
    res = ''
    i, j = m - 1, n - 1
    while i > 0 and j > 0:
        if flag[i][j] == 'ok':
            res += L[j - 1]
            i -= 1
            j -= 1
        elif flag[i][j] == 'left':
            j -= 1
        elif flag[i][j] == 'up':
            i -= 1
    return res[::-1]


L = 'abecbab'
S = 'bdcbabb'
num, flag = LCS(L, S)
res = printres(flag, L, S)
print(res)
