class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(nums+B)

    def maxProduct(nums):
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum