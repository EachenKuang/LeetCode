# https://leetcode.com/problems/word-subsets/description/
class Solution:
    def wordSubsets(self, A, B):
        uni = collections.Counter()
        for b in B:
            for c, n in collections.Counter(b).items():
                uni[c] = max(uni[c], n)
        res = []
        for a in A:
            count = collections.Counter(a)
            if all(count[c] >= uni[c] for c in uni):
                res.append(a)
        return res
    
    def wordSubsets(self, A, B):
        ccb={}
        for b in B:
            cb={}
            for l in b:
                if l in cb:
                    cb[l]+=1
                else:
                    cb[l]=1
            for l in b:
                if l not in ccb or ccb[l]<cb[l]:
                    ccb[l]=cb[l]

        ans=[]
        for a in A:
            flag=True
            for i in ccb:
                if a.count(i)<ccb[i]:
                    flag=False
                    break
            if flag:
                ans.append(a)
        return ans