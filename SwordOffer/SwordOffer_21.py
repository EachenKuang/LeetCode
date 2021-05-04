# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
#  
#
# 示例：
#
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
#  
#
# 提示：
#
# 0 <= nums.length <= 50000
# 1 <= nums[i] <= 10000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """
        前后双指针法
        first指向第一个，last指向最后一个，两个指针向中间靠拢
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        first, last = 0, len(nums) - 1
        while first < last:
            if nums[first] % 2 == 1:
                first += 1
                continue
            if nums[last] % 2 == 0:
                last -= 1
                continue
            nums[first], nums[last] = nums[last], nums[first]
        return nums

    def exchange_2(self, nums: List[int]) -> List[int]:
        """
        快慢双指针法
        low与fast同时从首位移动，fast 的作用是向前搜索奇数位置，low 的作用是指向下一个奇数应当存放的位置
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        low = fast = 0
        while fast < len(nums):
            if nums[fast] % 2 == 1:
                nums[fast], nums[low] = nums[low], nums[fast]
                low += 1
            fast += 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    test_suits = [
        [],
        [1],
        [0],
        [1, 3, 2, 4],
        [1, 2, 3, 4],
        [0, 0, 0, 0, 0, 1]
    ]
    for test_suit in test_suits:
        solution.exchange(test_suit)
        print(test_suit)
    for test_suit in test_suits:
        solution.exchange_2(test_suit)
        print(test_suit)