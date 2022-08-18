class InsertionSort:
    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            current = i - 1
            insert_value = nums[i]
            while current >= 0 and insert_value < nums[current]:
                # 调整需要插入的值，找到需要插入的位置，其到 current ~ i 统一右移
                nums[current + 1] = nums[current]
                current -= 1
            nums[current + 1] = insert_value
        return nums


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3, 4, 4, 7, 9]
    solution = InsertionSort()
    print(solution.insertion_sort(nums))