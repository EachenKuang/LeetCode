# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，
# 输出旋转数组的最小元素。例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
#
# 示例 1：
#
# 输入：[3,4,5,1,2]
# 输出：1
# 示例 2：
#
# 输入：[2,2,2,0,1]
# 输出：0
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
        第一眼看到这题，不就是求最小值吗！min就可以，然而不是这样的。
        """
        return min(numbers)

    def minArray2(self, numbers: List[int]) -> int:
        """
        递增数组的旋转，说明前半段和后半段是递增有序的，只需要找到中间截断部分，找出后半的第一个就是最小值
        """
        if len(numbers) == 0:
            return None
        if len(numbers) == 1:
            return numbers[0]
        for i in range(1, len(numbers)):
            former = numbers[i-1]
            latter = numbers[i]
            if former <= latter:
                continue
            else:
                return latter
        return numbers[0]

    def minArray3(self, numbers: List[int]) -> int:
        """
        说道排序，肯定要祭出我们的二分查找
        分三种情况：
        如果中间值
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            middle = left + (right - left) // 2
            if numbers[middle] < numbers[right]:
                # 如果中间值小于右值，说明中间值到右值是递增数列，右值可以移到中间值的位置
                right = middle
            elif numbers[middle] > numbers[right]:
                # 如果中间值大于右值，说明左值到中间值是递增数列，左值可以移到中间值的位置
                left = middle + 1
            else:
                # 如果中间值等于右值，这种情况下无法判断两边那边是递增
                # [3, 1, 3, 3, 3] 与 [3, 3, 3, 1, 3]
                # 这时可以右值左移一步
                right -= 1
        return numbers[left]


if __name__ == '__main__':
    input_items = [3, 4, 5, 6, 1, 2]
    solution = Solution()
    assert 1 == solution.minArray(input_items)
    assert 1 == solution.minArray2(input_items)
    assert 1 == solution.minArray3(input_items)