# https://github.com/Snailclimb/JavaGuide/blob/main/docs/cs-basics/algorithms/10-classical-sorting-algorithms.md
from typing import List


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def test_func_and_print(func, nums):
    temp_nums = nums.copy()
    print("original:{}".format(temp_nums))
    print("after {}:{}".format(func.__name__, func(temp_nums)))


def bubble_sort(nums: List[int]) -> List[int]:
    """
    冒泡排序 (Bubble Sort)
    冒泡排序是一种简单的排序算法。它重复地遍历要排序的序列，依次比较两个元素，如果它们的顺序错误就把它们交换过来。
    遍历序列的工作是重复地进行直到没有再需要交换为止，此时说明该序列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢 “浮” 到数列的顶端。

    算法步骤
    1.比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    3.针对所有的元素重复以上的步骤，除了最后一个；
    4.重复步骤 1~3，直到排序完成。

    此处对代码做了一个小优化，加入了 is_sorted Flag，目的是将算法的最佳时间复杂度优化为 O(n)，
    即当原输入序列就是排序好的情况下，该算法的时间复杂度就是 O(n)。

    算法分析
    稳定性：稳定
    时间复杂度 ：最佳：O(n) ，最差：O(n^2)， 平均：O(n^2)
    空间复杂度 ：O(1)
    排序方式 ：In-place
    """
    length = len(nums)
    for i in range(length):
        is_sorted = True
        for j in range(0, length - 1):
            if nums[j] > nums[j + 1]:
                # 交换相邻的位置
                swap(nums, j, j + 1)
                is_sorted = False
        # 如果没有交换，说明整体的顺序是排好序的，可以直接跳出循环
        if is_sorted:
            break
    return nums


def select_sort(nums: List[int]) -> List[int]:
    """
    选择排序 (Selection Sort)
    选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。
    唯一的好处可能就是不占用额外的内存空间了吧。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

    算法步骤
    1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3.重复第 2 步，直到所有元素均排序完毕。

    算法分析
    稳定性：不稳定
    时间复杂度 ：最佳：O(n^2) ，最差：O(n^2)， 平均：O(n^2)
    空间复杂度 ：O(1)
    排序方式 ：In-place
    """
    length = len(nums)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_index]:
                min_index = j
        # 找到一轮最小的index，与 index为i的数进行交换
        if min_index != i:
            swap(nums, min_index, i)
    return nums


def insertion_sort(nums):
    """
    插入排序 (Insertion Sort)
    插入排序是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    插入排序在实现上，通常采用 in-place 排序（即只需用到 O(1) 的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

    插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能够秒懂。
    插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

    插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。

    算法步骤
    1.从第一个元素开始，该元素可以认为已经被排序；
    2.取出下一个元素，在已经排序的元素序列中从后向前扫描；
    3.如果该元素（已排序）大于新元素，将该元素移到下一位置；
    4.重复步骤 3，直到找到已排序的元素小于或者等于新元素的位置；
    5.将新元素插入到该位置后；
    6.重复步骤 2~5。

    算法分析
    稳定性：稳定
    时间复杂度 ：最佳：O(n) ，最差：O(n2)， 平均：O(n2)
    空间复杂度 ：O(1)
    排序方式 ：In-place
    """
    length = len(nums)
    for i in range(1, length):
        pre_index = i - 1
        current = nums[i]
        while pre_index >= 0 and current < nums[pre_index]:
            nums[pre_index + 1] = nums[pre_index]
            pre_index -= 1
        nums[pre_index + 1] = current
    return nums


def insertion_sort2(nums):
    """
    与方法 insertion_sort 原理是一致的，可能更好理解一些
    """
    length = len(nums)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if nums[j] > nums[j - 1]:
                break
            else:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


def shell_sort(nums):
    """
    希尔排序 (Shell Sort)
    希尔排序是希尔 (Donald Shell) 于 1959 年提出的一种排序算法。希尔排序也是一种插入排序，它是简单插入排序经过改进之后的一个更高效的版本，
    也称为递减增量排序算法，同时该算法是冲破 O(n²) 的第一批算法之一。

    希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录 “基本有序” 时，再对全体记录进行依次直接插入排序。

    算法步骤
    我们来看下希尔排序的基本步骤，在此我们选择增量 gap=length/2，缩小增量继续以 gap = gap/2 的方式，这种增量选择我们可以用一个序列来表示，
    {n/2, (n/2)/2, ..., 1}，称为增量序列。希尔排序的增量序列的选择与证明是个数学难题，我们选择的这个增量序列是比较常用的，也是希尔建议的增量，
    称为希尔增量，但其实这个增量序列不是最优的。此处我们做示例使用希尔增量。

    先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：
    1.选择一个增量序列 {t1, t2, …, tk}，其中 (ti>tj, i<j, tk=1)；
    2.按增量序列个数 k，对序列进行 k 趟排序；
    3.每趟排序，根据对应的增量 t，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

    算法分析
    稳定性：稳定
    时间复杂度 ：最佳：O(nlogn)， 最差：O(n2) 平均：O(nlogn)
    空间复杂度 ：O(n)
    """
    length = len(nums)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            current = nums[i]
            pre_index = i - gap
            while pre_index >= 0 and nums[pre_index] > current:
                nums[pre_index + gap] = nums[pre_index]
                pre_index -= gap
            nums[pre_index + gap] = current
        gap //= 2
    return nums


def merge_sort(nums):
    """
    归并排序 (Merge Sort)
    归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法 (Divide and Conquer) 的一个非常典型的应用。归并排序是一种稳定的排序方法。
    将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为 2 - 路归并。

    和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间。

    算法步骤
    归并排序算法是一个递归过程，边界条件为当输入序列仅有一个元素时，直接返回，具体过程如下：
    1.如果输入内只有一个元素，则直接返回，否则将长度为 n 的输入序列分成两个长度为 n/2 的子序列；
    2.分别对这两个子序列进行归并排序，使子序列变为有序状态；
    3.设定两个指针，分别指向两个已经排序子序列的起始位置；
    4.比较两个指针所指向的元素，选择相对小的元素放入到合并空间（用于存放排序结果），并移动指针到下一位置；
    5.重复步骤 3 ~4 直到某一指针达到序列尾；
    6.将另一序列剩下的所有元素直接复制到合并序列尾。

    算法分析
    稳定性：稳定
    时间复杂度 ：最佳：O(nlogn)， 最差：O(nlogn)， 平均：O(nlogn)
    空间复杂度 ：O(n)
    """

    def merge(nums_a: List[int], nums_b: List[int]) -> List[int]:
        ans = []
        i = 0
        j = 0
        while i < len(nums_a) and j < len(nums_b):
            if nums_a[i] <= nums_b[j]:
                ans.append(nums_a[i])
                i += 1
            else:
                ans.append(nums_b[j])
                j += 1
        ans.extend(nums_a[i:])
        ans.extend(nums_b[j:])
        return ans

    length = len(nums)
    if length <= 1:
        return nums
    middle = length // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)


def quick_sort(nums):
    """
    快速排序 (Quick Sort)
    快速排序用到了分治思想，同样的还有归并排序。乍看起来快速排序和归并排序非常相似，都是将问题变小，先排序子串，最后合并。
    不同的是快速排序在划分子问题的时候经过多一步处理，将划分的两组数据划分为一大一小，这样在最后合并的时候就不必像归并排序那样再进行比较。但也正因为如此，划分的不定性使得快速排序的时间复杂度并不稳定。

    快速排序的基本思想：通过一趟排序将待排序列分隔成独立的两部分，其中一部分记录的元素均比另一部分的元素小，则可分别对这两部分子序列继续进行排序，以达到整个序列有序。

    算法步骤
    快速排序使用分治法（Divide and conquer）策略来把一个序列分为较小和较大的 2 个子序列，然后递回地排序两个子序列。具体算法描述如下：

    1. 从序列中随机挑出一个元素，做为 “基准”(pivot)；
    2. 重新排列序列，将所有比基准值小的元素摆放在基准前面，所有比基准值大的摆在基准的后面（相同的数可以到任一边）。
    在这个操作结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    3. 递归地把小于基准值元素的子序列和大于基准值元素的子序列进行快速排序。

    算法分析
    稳定性 ：不稳定
    时间复杂度 ：最佳：O(nlogn)， 最差：O(nlogn)，平均：O(nlogn)
    空间复杂度 ：O(nlogn)
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

    def quick(nums: List[int], left, right):
        if left >= right:
            return
        pivot = partition(nums, left, right)
        quick(nums, left, pivot - 1)
        quick(nums, pivot + 1, right)

    quick(nums, 0, len(nums) - 1)
    return nums


def quick_sort2(nums: List[int]):
    """
    递归法实现
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


def heap_sort(nums):
    """
    堆排序 (Heap Sort)
    堆排序是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆的性质：即子结点的值总是小于（或者大于）它的父节点。

    算法步骤
    1.将初始待排序列 (R1, R2, ……, Rn) 构建成大顶堆，此堆为初始的无序区；
    2.将堆顶元素 R[1] 与最后一个元素 R[n] 交换，此时得到新的无序区 (R1, R2, ……, Rn-1) 和新的有序区 (Rn), 且满足 R[1, 2, ……, n-1]<=R[n]；
    3.由于交换后新的堆顶 R[1] 可能违反堆的性质，因此需要对当前无序区 (R1, R2, ……, Rn-1) 调整为新堆，然后再次将 R [1] 与无序区最后一个元素交换，
    得到新的无序区 (R1, R2, ……, Rn-2) 和新的有序区 (Rn-1, Rn)。不断重复此过程直到有序区的元素个数为 n-1，则整个排序过程完成。

    算法分析
    稳定性 ：不稳定
    时间复杂度 ：最佳：O(nlogn)， 最差：O(nlogn)， 平均：O(nlogn)
    空间复杂度 ：O(1)
    """

    def build_max_heap(nums):
        """
        构建成大顶堆
        从最后一个节点的父节点开始往前遍历
        对于 i 节点，它的左右节点分别为 2i+1,2i+2
        当最后一个节点为 index n，那么其父节点是 n//2-1
        """
        for i in range(len(nums) // 2 - 1, -1, -1):
            heapify(nums, i)

    def heapify(nums, i):
        """
        将 index 为 i 的元素与 堆顶替换，然后调整堆，O()
        """
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i
        if right < heap_len and nums[right] > nums[largest]:
            largest = right
        if left < heap_len and nums[left] > nums[largest]:
            largest = left
        if largest != i:
            # 调换左右节点大的与index i的节点
            swap(nums, largest, i)
            # 因为调换了节点，需要对 index largest 进行递归调整
            heapify(nums, largest)

    heap_len = len(nums)  # 全局变量，每次堆顶替换后，需要减一
    build_max_heap(nums)
    for i in range(heap_len - 1, 0, -1):
        swap(nums, 0, i)
        heap_len -= 1
        heapify(nums, 0)
    return nums


if __name__ == '__main__':
    nums = [3, 5, 6, 2, 8]
    # 冒泡排序
    test_func_and_print(bubble_sort, nums)
    # 选择排序
    test_func_and_print(select_sort, nums)
    # 插入排序
    test_func_and_print(insertion_sort, nums)
    test_func_and_print(insertion_sort2, nums)
    # 希尔排序
    test_func_and_print(shell_sort, nums)
    # 归并排序
    test_func_and_print(merge_sort, nums)
    # 快速排序
    test_func_and_print(quick_sort, nums)
    test_func_and_print(quick_sort2, nums)
    # 堆排序
    test_func_and_print(heap_sort, nums)
