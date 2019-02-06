class Solution(object):
    def countPairsLTE(self, array, value):
        ans = 0
        for i in range(len(array)):
            ans += bisect.bisect_right(array, array[i] + value, lo = i) - i - 1
        return ans
        
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        low, high = min([abs(nums[i] - nums[i+1]) for i in range(len(nums) - 1)]), abs(nums[0] - nums[~0])
        while low < high:
            mid = (low + high)//2
            if self.countPairsLTE(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        return low