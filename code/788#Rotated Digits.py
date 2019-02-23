# https://leetcode.com/problems/rotated-digits/description/
class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1,N+1):
            temp = str(i)
            if '3' in temp or '4' in temp or '7' in temp:
                continue
            if '6' in temp or '9' in temp or '2' in temp or '5' in temp:
                res+=1
        return res
    
    def rotatedDigits1(self, N):
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])
        def isGood(x):    
            s = set([int(i) for i in str(x)])
            return s.issubset(s2) and not s.issubset(s1)
        return sum(isGood(i) for i in range(N + 1))
    
    def rotatedDigits(self, N):
        a = [0, 1, 2, 5, 6, 8, 9]
        b = [0, 1, 8]
        
	    def helper(candis, N):
	        
	        NS = str(N)
	        if len(NS) == 1:
	            i = bisect.bisect_left(candis, N)
	            if i < len(candis) and candis[i] == N:
	                i += 1
	            return i
	        first = int(NS[0])
	        i = bisect.bisect_left(candis, first)
	        # 如果第一位取的数字小于first，那么后面都可以取 9 
	        # 如果第一位取的数字等于first，那么后面的算int(NS[1:]) 就可以
	        b = (10**(len(NS) - 1)) - 1
	        if i < len(candis) and candis[i] == first:
	            a =  i*helper(candis, b) + helper(candis, int(NS[1:]))
	            return a 
	        else:
	            a =  i*helper(candis, b)
	            return a
	                    
	    return helper(a, N) - helper(b, N)          