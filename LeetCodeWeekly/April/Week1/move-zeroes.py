# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order
# of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[point_zero] = nums[i]
                point_zero += 1
        for j in range(point_zero, len(nums)):
            nums[j] = 0


if __name__ == '__main__':
    solution = Solution()
    before = [0, 1, 0, 3, 12]
    after = [1, 3, 12, 0, 0]
    solution.moveZeroes(before)
    assert before == after
    before = [0, 1, 0, 0, 0]
    after = [1, 0, 0, 0, 0]
    solution.moveZeroes(before)
    assert before == after
