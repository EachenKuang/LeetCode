# https://leetcode.com/problems/max-consecutive-ones/description/
class Solution:
    # 1  beat 80%
    # 找零
    # 通过计算每两个零之间的距离，找最大的值
    # 注意：
    # 1、存在没有零的情况，所以需要设置一个-1的零位以及一个len(nums)的零位
    # 2、在循环结束后计算末尾位的1
    # 3、用下标相减时需要额外减1
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = max(count, i - res - 1)
                res = i
        count = max(count, len(nums) - res -1)
        return count
    # 2 
    # 直接数1法
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        for n in nums:
            if n:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count
    # 3 
    # 把数组当成一个string，利用split('0')
    # 分割成多个长度字符串，计算最大长度
    # 下面是100%的答案，利用bytearray将数组转化为
    # a = [1,1,0,1,1,0,1,1,1]
    # bytearray(a)
    # bytearray(b'\x01\x01\x00\x01\x01\x00\x01\x01\x01')
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = bytearray(nums).split(b'\x00')
        return max([len(i) for i in temp])
