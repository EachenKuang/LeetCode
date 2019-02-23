# https://leetcode.com/problems/optimal-division/description/
class Solution:
    # 1
    # 对于a/b/c/d/e
    # 最大应该是 a*c*d*e/b 等价于 a/(b/c/d/e)
    # 策略：
    # 1）只有一个数，本身
    # 2）只有两个数，a/b
    # 3）两个以上的数需要添加括号： a/(b/c)
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)==1:
            return str(nums[0])
        elif len(nums)==2:
            return str(nums[0])+'/'+str(nums[1])
        else:
            return "{0}/({1})".format(nums[0],'/'.join(map(str,nums[1:])))