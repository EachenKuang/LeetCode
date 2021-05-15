# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
#  
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#  
#
# 示例 1:
#
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2
#  
#
# 限制：
#
# 1 <= 数组长度 <= 50000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += (1 if num == x else -1)
        return x


    def majorityElement_2(self, nums: List[int]) -> int:
        """
        遍历一次，找到超过n/2的个数的数字
        """
        count_mapping = dict()
        length = len(nums)
        for num in nums:
            if num in count_mapping:
                count_mapping[num] += 1
                if count_mapping[num] > length//2:
                    return num
            else:
                count_mapping[num] = 1
        return None


if __name__ == '__main__':
    items = [
        [1, 2, 3, 2, 2, 2, 5, 4, 2]
    ]
    results = [2]
    solution = Solution()
    for item, result in zip(items, results):
        print(solution.majorityElement(item))
        assert result == solution.majorityElement(item)