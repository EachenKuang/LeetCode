
# https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
# 求只出现1次的两个数
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:


        # 利用异或的性质
        # 按位分组
        a_xor_b = 0
        for i in nums:
            a_xor_b ^= i
        
        # 找到最低位的一
        low_bit_one = a_xor_b & (-a_xor_b)

        res = 0
        for i in nums:
            if low_bit_one & i:
                res ^= i

        return [res, a_xor_b ^ res]