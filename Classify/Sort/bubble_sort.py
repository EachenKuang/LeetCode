class BubbleSort:
    def bubble_sort(self, nums):
        for i in range(len(nums)):
            is_sort = False
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j+1]:
                    # 交换，每次将最大的数放置在 len-i-1
                    is_sort = True
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            if not is_sort:
                return nums
        return nums


if __name__ == '__main__':
    nums = [1, 1, 3, 2, 3, 4, 10, 7, 9]
    solution = BubbleSort()
    print(solution.bubble_sort(nums))