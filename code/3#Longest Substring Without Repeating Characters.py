class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # method 1: using set 
        """
        res = 0
        i = 0
        j = 0
        l = len(s)
        mySet = set()
        while i<l and j <l:
            if not mySet.__contains__(s[j]):
                mySet.add(s[j])
                j += 1
                res = max(j-i,res)
            else:
                mySet.remove(s[i])
                i += 1
        return res
        """
        # method 2: using dict
        res = 0
        i = 0
        j = 0
        l = len(s)
        myDict = dict()
        while i<l and j <l:            
            if myDict.__contains__(s[j]):
                i = max(myDict[s[j]], i)                    
            res = max(res, j-i+1)
            myDict[s[j]] = j+1
            j +=1

        return res
                
            
