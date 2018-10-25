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
import random
def quickSort(nums):
	"""
	快速排序通过一个切分元素将数组分为两个子数组，
	左子数组小于等于切分元素，右子数组大于等于切分元素，
	将这两个子数组排序也就将整个数组排序了。
	:paramnums:
	:return:
	"""
	def partion(nums,left,right):
	"""
	取num[left]作为切分元素，然后从数组的左端向右扫描直到找到第一个大于等于它的元素，
	再从数组的右端向左扫描找到第一个小于等于它的元素，交换这两个元素，并不断进行这个过程，
	就可以保证左指针i的左侧元素都不大于切分元素，右指针j的右侧元素都不小于切分元素。
	当两个指针相遇时，将切分元素a[left]和a[j]交换位置。
	:paramnums:
	:paramleft:
	:paramright:
	:return:
	"""
	i=left+1
	j=right
	temp=nums[left]
	while True:
		while nums[i]<=tempandi!=right:
			i+=1
		while nums[j]>=tempandj!=left:
			j-=1
		if i>=j:
			break
		nums[i],nums[j]=nums[j],nums[i]
		nums[left],nums[j]=nums[j],nums[left]
	return j

	def sort(nums,left,right):
		"""
		:paramnums:
		:paramleft:
		:paramright:
		:return:
		"""
		if left<right:
			div=partion(nums,left,right)
			sort(nums,left,div-1)
			sort(nums,div+1,right)
		return nums

	random.shuffle(nums)
	return sort(nums,0,len(nums)-1)


print("quickSort(3,5,2,4,1,4,6,32,5,6)",quickSort([3,5,2,4,1,4,6,32,5,6]))
#-----------------------------------------------------------------------------


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


	defmergeSort(nums):
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
