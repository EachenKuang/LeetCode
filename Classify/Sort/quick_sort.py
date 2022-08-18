class QuickSort:
    def quick_sort(self, nums):
        return self.quick(nums, 0, len(nums) - 1)

    def partition(self, nums, i, j) -> int:
        # 以最前的数作为基准
        pivot = nums[i]
        left = i
        right = j
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            while left < right and nums[left] <= pivot:
                left += 1
            # 交换
            nums[left], nums[right] = nums[right], nums[left]
        # 交换基准与分割点的位置
        nums[i], nums[left] = nums[left], nums[i]
        return left

    def quick(self, nums, i, j):
        if i >= j:
            # 需要控制结束条件
            return nums
        pivot_index = self.partition(nums, i, j)
        self.quick(nums, i, pivot_index - 1)
        self.quick(nums, pivot_index + 1, j)
        return nums


if __name__ == '__main__':
    nums = [10, 13, 2, 33, 3, 4, 4, 7, 9]
    solution = QuickSort()
    print(solution.quick_sort(nums))