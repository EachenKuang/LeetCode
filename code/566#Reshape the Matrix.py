# https://leetcode.com/problems/reshape-the-matrix/description/
class Solution(object):
	# 1 常规
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            items = [y for x in nums for y in x]
            return [items[x*c : ((x+1)*c)] for x in range(r)]
    # 2 
    # 巧妙运用各种函数
    def matrixReshape(self, nums, r, c):
	    flat = sum(nums, [])
	    if len(flat) != r * c:
	        return nums
	    tuples = zip(*([iter(flat)] * c))
	    return map(list, tuples)
        
        
        