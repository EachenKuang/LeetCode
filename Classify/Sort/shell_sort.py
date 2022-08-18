class ShellSort:
    def shell_sort(self, nums):
        n = len(nums)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                current = i - gap
                insert_value = nums[i]
                while current >= 0 and insert_value < nums[current]:
                    # 调整需要插入的值，找到需要插入的位置，其到 current ~ i 统一右移
                    nums[current + gap] = nums[current]
                    current -= gap
                nums[current + gap] = insert_value
            gap //= 2
        return nums


if __name__ == '__main__':
    nums = [10, 13, 2, 33, 3, 4, 4, 7, 9]
    solution = ShellSort()
    print(solution.shell_sort(nums))