# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    # 1
    # def searchRange(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     l = 0
    #     r = len(nums)
    #     while l<r:
    #         m = l + (r - l)//2
    #         if target <= nums[m]:
    #             r = m
    #         else:
    #             l = m + 1
    #     return l

    # 2
    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return [left, right] if left <= right else [-1, -1]

if __name__ == '__main__':
    t = Solution()
    print(t.searchRange([1,2,3,3,3,4,4,6],2))