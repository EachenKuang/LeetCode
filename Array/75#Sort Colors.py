# https://leetcode.com/problems/sort-colors/description/
from collections import Counter

# 1 直接sort
def sortColors1(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums.sort()

# 2 利用字典，计算出0，1，2的个数
def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    c = Counter(nums)
    nums[:] = [0] * c[0] + [1] * c[1] + [2] * c[2]

# 3 使用堆heapq
def sortColors3(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    import heapq
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    i = 0
    while heap:
        nums[i] = heapq.heappop(heap)
        i += 1

def sortColors4(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    def swap(arr, i1, i2):
        temp = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = temp

    ptr0 = 0
    ptr1 = 0
    ptr2 = 0
    mainPtr = 0
    while mainPtr < len(nums):
        if nums[mainPtr] == 0:
            nums.insert(ptr0, nums.pop(mainPtr))
            ptr1 += 1
            ptr2 += 1
        elif nums[mainPtr] == 1:
            nums.insert(ptr1, nums.pop(mainPtr))
            ptr2 += 1
        elif nums[mainPtr] == 2:
            nums.insert(ptr2, nums.pop(mainPtr))
        mainPtr += 1
