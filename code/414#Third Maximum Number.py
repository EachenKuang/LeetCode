# https://leetcode.com/problems/third-maximum-number/description/
class Solution(object):
    # 1 
    # 先转化为set
    # 转化为list排序
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        return sorted(list(a))[-3 if len(a)>=3 else -1]
    # 2
    def thirdMax(self, nums):     
        if len(nums) < 3:
            return max(nums)
        else:
            newNums = set(nums)
            if len(newNums) <3:
                return max(newNums)
            else:
                newNums = sorted(newNums)
                return newNums[len(newNums)-3]