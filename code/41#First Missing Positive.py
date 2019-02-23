# https://leetcode.com/problems/first-missing-positive/description/
class Solution:
    # 1 
    # 先找出最大数m，构造一个1到m+1的集合M
    # 用集合M减去nums集合N生成的集合M-N
    # 消失的最小正数就是min(M-N)
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        max_num = max(nums)        
        return min(set(range(1,max_num+2))-set(nums))
    # 2 
    # 使用循环，从1遍历到len(nums)+1
    def firstMissingPositive(self, nums):
        if len(nums)==0:
            return 1
        #nums.sort()
      #  if nums[0]>1:
       #     return 1
        for i in range(1,len(nums)+2):
            if i not in nums:
                return i