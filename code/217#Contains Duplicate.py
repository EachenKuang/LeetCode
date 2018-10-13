# https://leetcode.com/problems/contains-duplicate-ii/description/
class Solution(object):
    # 本题在 contains-duplicate 的基础上增加了一个k的限制
    # 那么最基本的方法是对同样的数的下标之差判断
    # 1 常规方法
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapping = dict()
        for i,n in enumerate(nums):
            if n in mapping and i-mapping[n]<=k:
                return True
            else:
                mapping[n]=i
        return False
    # 2 效率比较高
    # leetcode击败100%的对手
    # 也是在I中巧妙方式的基础上改进的
    # 先用set判断是否有重复的数，然后再进行遍历
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        if len(set(nums)) == len(nums):
            return False
        
        l = len(nums)
        for i in range(l):
            j = 1
            while j <= k and i + j < l:
                if nums[i] == nums[i + j]:
                    return True
                j += 1
        return False