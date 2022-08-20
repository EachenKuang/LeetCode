
# https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 双指针法
        left = 1
        right = 2
        ans = []
        while left < right and right < target:
            sum = (right - left + 1) * (right + left) //2
            if sum == target:
                ans.append([i for i in range(left, right + 1)])
                left += 1
            elif sum > target:
                left += 1
            else:
                right += 1
        return ans
