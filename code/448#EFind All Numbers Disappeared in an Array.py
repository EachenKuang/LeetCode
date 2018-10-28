# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
	# 1 
	# 先使用set,然后遍历1-n,将不在set中的取出
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        num_set = set(nums)
        res = []
        for i in range(1,length+1):
            if i not in num_set:
                res.append(i)
        return res
    # 2 使用两个set相减，耗时长
    def findDisappearedNumbers2(self,nums):
        all_nums = [i for i in range(1, len(nums)+1)]
        return list(set(all_nums) - set(nums))