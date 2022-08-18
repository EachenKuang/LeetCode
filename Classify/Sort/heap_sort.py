def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


class HeapSort:

    def __init__(self, nums):
        # 初始化全局变量，堆剩下还需要排序的长度
        self.heap_len = len(nums)

    def heapify(self, nums, i):
        """
        调整以 i 为根节点的堆，使之成为大根堆
        这里使用递归的方式
        """
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2
        if left < self.heap_len and nums[largest] < nums[left]:
            largest = left
        if right < self.heap_len and nums[largest] < nums[right]:
            largest = right
        if largest != i:
            # 交换
            swap(nums, largest, i)
            self.heapify(nums, largest)

    def build_heap(self, nums):
        for i in range(self.heap_len // 2 - 1, -1, -1):
            self.heapify(nums, i)

    def heap_sort(self, nums):
        self.build_heap(nums)
        while self.heap_len > 0:
            # 交换
            swap(nums, self.heap_len - 1, 0)
            self.heap_len -= 1
            self.heapify(nums, 0)
        return nums


if __name__ == '__main__':
    nums = [3, 4, 1, 2, 7, 9, 3, 4, 1]
    solution = HeapSort(nums)
    print(solution.heap_sort(nums))

