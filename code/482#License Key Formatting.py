# https://leetcode.com/problems/license-key-formatting/description/
class Solution:
    # 理解题目意思很重要

    def licenseKeyFormatting(self, S, K):
        S=S.upper()
        listS = S.split("-")
        full = "".join(listS)
        full = full[::-1]
        if K!= 0:
            newsplit = [full[K*i:K*(i+1)] for i in range(1+len(full)//K)]
            if newsplit[-1] == "":
                newsplit.pop(-1)
            return "-".join(newsplit)[::-1]

        else:
            return full[::-1]