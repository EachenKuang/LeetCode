# https://leetcode.com/problems/contains-duplicate/description/
class Solution(object):
    # 1 常规方法 使用字典记录，利用字典查找O(1)
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapping = dict()
        for i in nums:
            if i in mapping:
                return True
            else:
                mapping[i]=1
        return False
    # 2 巧妙地方法 利用set方法
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(set(nums)) == len(nums)):
            return False 
        return True
    # 3 先sort，然后比较相邻是否相同，不推荐
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False