# https://leetcode.com/problems/degree-of-an-array/description/
class Solution(object):
    		    
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: 
            	left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans
    def findShortestSubArray(self, nums):
        c = Counter(nums)
        count = max(c.values())
        if count == 1:
            return 1
        rnums = nums[-1::-1]
        
        return len(nums) - max([rnums.index(n) + nums.index(n) for (n, val) in c.items() if val == count])
