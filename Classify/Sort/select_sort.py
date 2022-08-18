class SelectSort:
    def select_sort(self, nums):
        for i in range(len(nums)-1):
            min_index = i
            for j in range(i+1, len(nums)):
                # 寻找 i~n 中最小的数，然后放置到 i
                if nums[min_index] > nums[j]:
                    min_index = j
            # 交换
            if min_index != i:
                nums[min_index], nums[i] = nums[i], nums[min_index]
        return nums


if __name__ == '__main__':
    nums = [10, 13, 2, 33, 3, 4, 4, 7, 9]
    solution = SelectSort()
    print(solution.select_sort(nums))
