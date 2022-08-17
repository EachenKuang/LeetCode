#排序
#插入排序
def insertSort(nums):
	"""
	插入排序从左到右进行，每次都将当前元素插入到左侧已经排序的数组中，使得插入之后左部数组依然有序。
	第j元素是通过不断向左比较并交换来实现插入过程：当第j元素小于第j-1元素，
	就将它们的位置交换，然后令j指针向左移动一个位置，不断进行以上操作。
	:paramnums:int
	:returnnums:int
	"""
	n =len(nums)
	for i in range(1,n):
		for j in range(i,0,-1):
			if nums[j]>nums[j-1]:
				break
			else:
				nums[j],nums[j-1]=nums[j-1],nums[j]
	return nums


print("insertSort(3,5,2,4,1)",insertSort([3,5,2,4,1]))
#-----------------------------------------------------------------------------

#选择排序
def selectSort(nums):
	"""
	选择出数组中的最小元素，将它与数组的第一个元素交换位置。
	再从剩下的元素中选择出最小的元素，将它与数组的第二个元素交换位置。
	不断进行这样的操作，直到将整个数组排序。
	:paramnums:int
	:returnnums:int
	"""
	n=len(nums)
	for i in range(n):
		min_index=i
		for j in range(i,n):
			if nums[j]<nums[min_index]:
				min_index=j
			nums[i],nums[min_index]=nums[min_index],nums[i]
	return nums


print("selectSort(3,5,2,4,1)",selectSort([3,5,2,4,1]))
#-----------------------------------------------------------------------------


#冒泡排序
def bubbleSort(nums):
	"""
	通过从左到右不断交换相邻逆序的相邻元素，在一轮的交换之后，
	可以让未排序的元素上浮到最右侧，是的右侧是已排序的。
	在一轮交换中，如果没有发生交换，就说明数组已经是有序的，此时可以直接退出。
	:paramnums:
	:return:
	"""
	n=len(nums)
	for i in range(n):
		for j in range(i+1,n):
			if nums[j]<nums[i]:
				nums[i],nums[j]=nums[j],nums[i]
	return nums


print("bubbleSort(3,5,2,4,1)",bubbleSort([3,5,2,4,1]))
#-----------------------------------------------------------------------------

#快速排序
from typing import List

def quick_sort(nums: List[int]):
	"""
	递归方法实现快排
	"""
	def quick(nums: List[int], l: int, r: int):
		if l >= r:
			return nums
		# 哨兵划分操作（以 nums[l] 作为基准数）
		i = l
		j = r
		while i < j:
			# 从右往左，查找首个小于基准的数
			while i < j and nums[j] >= nums[l]: 
				j -= 1
			# 从左往右，查找首个大于基准的数
			while i < j and nums[i] <= nums[l]: 
				i += 1
			nums[i], nums[j] = nums[j], nums[i]
		nums[l], nums[i] = nums[i], nums[l]
		# 递归左（右）子数组执行哨兵划分
		quick(nums, l, i - 1)
		quick(nums, i + 1, r)
		return nums
	return quick(nums, 0, len(nums) - 1)

print("quick_sort(3,5,2,4,1,4,6,32,5,6)",quick_sort([3,5,2,4,1,4,6,32,5,6]))

def quick_sort_partition(nums: List[int]):

	def partition(nums: List[int], l, r) -> int:
		if l >= r:
			return l
		# 这里使用最左边作为哨兵
		i, j = l, r
		while i < j:
			# 从右往左，查找首个小于基准的数
			while i < j and nums[j] >= nums[l]: 
				j -= 1
			# 从左往右，查找首个大于基准的数
			while i < j and nums[i] <= nums[l]: 
				i += 1
			nums[i], nums[j] = nums[j], nums[i]
		nums[l], nums[i] = nums[i], nums[l]
		return i
	
	def quick(nums: List[int], left, right):
		if left >= right:
			return
		pivot = partition(nums, left, right)
		quick(nums, left, pivot -1)
		quick(nums, pivot + 1, right)
	
	quick(nums, 0, len(nums)-1)
	return nums
		
print("quick_sort_partition(3,5,2,4,1,4,6,32,5,6)",quick_sort_partition([3,5,2,4,1,4,6,32,5,6]))

def quick_sort_stack(nums: List[int]):
	"""
	上面使用的是递归，实际上，可以通过stack的方法来实现非递归
	"""
	def partition(nums: List[int], l, r) -> int:
		if l >= r:
			return l
		# 这里使用最左边作为哨兵
		i, j = l, r
		while i < j:
			# 从右往左，查找首个小于基准的数
			while i < j and nums[j] >= nums[l]: 
				j -= 1
			# 从左往右，查找首个大于基准的数
			while i < j and nums[i] <= nums[l]: 
				i += 1
			nums[i], nums[j] = nums[j], nums[i]
		nums[l], nums[i] = nums[i], nums[l]
		return i
	
	left = 0
	right = len(nums)-1
	stack = [(left, right)]
	while stack:
		l, r = stack.pop()
		if l > r:
			continue
		pivot = partition(nums, l, r)
		stack.insert(0, (l, pivot - 1)) 
		stack.insert(0, (pivot + 1, r)) 
	return nums

print("quick_sort_stack(3,5,2,4,1,4,6,32,5,6)",quick_sort_stack([3,5,2,4,1,4,6,32,5,6]))


#归并排序
def merge(left,right):
	"""
	归并两个已经排好序的数组
	:paramnums1:
	:paramnums2:
	:return:
	"""
	i,j=0,0
	result=[]
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	result+=left[i:]
	result+=right[j:]
	return result


def mergeSort(nums):
	"""
	归并排序的思想是将数组分成两部分，分别进行排序，然后归并起来。
	:paramnums:
	:return:
	"""
	if len(nums)<=1:
		return nums
	middle=len(nums)//2
	left=mergeSort(nums[:middle])
	right=mergeSort(nums[middle:])
	return merge(left,right)

print("mergeSort(3,5,2,4,1,4,6,32,5,6)",mergeSort([3,5,2,4,1,4,6,32,5,6]))


#堆排序
