# https://leetcode.com/problems/house-robber/description/
class Solution:
    # 1 使用一个数组保存，动态规划
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        memo = [0 for _ in range(len(nums)+1)]
        memo[1] = nums[0]
        for i in range(1,len(nums)):
            memo[i+1] = max(memo[i],memo[i-1]+nums[i])
        return memo[len(nums)]
    
    # 2 将方法1中的数组简化为两个变量保存
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
        if not nums:
            return 0
        pre1 = 0
        pre2 = 0
        i = 0
        for num in nums:
            temp = pre1
            pre1 = max(pre2+num,pre1)
            pre2 = temp
        return pre1