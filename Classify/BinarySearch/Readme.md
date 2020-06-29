# 二分搜索
## 背景
### 它是如何工作的
在最简单的形式中，二进制搜索在具有指定左右索引的连续序列上运行。这称为搜索空间。二进制搜索维护搜索空间的左，右和中间标记，并比较搜索目标或将搜索条件应用于集合的中间值; 如果条件不满意或值不相等，则消除目标不能说谎的一半，并继续搜索剩下的一半，直到成功为止。如果搜索以空半部分结束，则无法满足条件并且未找到目标。

在接下来的章节中，我们将回顾如何识别二进制搜索问题，我们使用二进制搜索的原因，以及您可能以前不知道的3种不同的二进制搜索模板。由于二元搜索是一个常见的访谈主题，我们还会将练习问题分类到不同的模板，以便您可以练习使用每个模板。

**注意**：
二进制搜索可以采用许多替代形式，并且可能并不总是像搜索特定值那样直截了当。有时您必须应用特定条件或规则来确定接下来要搜索的哪一侧（左侧或右侧）。

### Binary Search
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

```
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
```
解答：
```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1 

```

### 识别和模板介绍
#### 我们如何识别二进制搜索？
如前所述，二进制搜索是一种算法，在每次比较后将搜索空间划分为2。每次需要搜索集合中的索引或元素时，都应考虑二进制搜索。如果集合是无序的，我们总是可以在应用二进制搜索之前对其进行排序。

####3个成功的二进制搜索部分
二进制搜索通常由3个主要部分组成：  

- 预处理：如果集合未排序则排序。  
- 二进制搜索：在每次比较后使用循环或递归将搜索空间分成两半。
- 后处理：确定剩余空间中的可行候选者。

####3个二进制搜索模板
当我们第一次学习二进制搜索时，我们可能会挣扎。我们可能会在线研究数百个二进制搜索问题，每次我们查看开发人员的代码时，它的实现似乎都略有不同。尽管每个实现在每个步骤中将问题空间划分为1/2，但是其中一个有很多问题：

* 为什么它的实施略有不同？ 
* 开发人员在想什么？  
* 哪种方式更容易？  
* 哪种方式更好？  

经过多次失败的尝试和大量的拉毛，我们找到了3个二进制搜索的主要模板。为了防止脱毛并使新开发人员更容易学习和理解，我们在下一章中提供了它们。

## 模板一
### 二分搜索模板一
#### 关键代码
```py
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
```
#### 注意事项
关键属性：

- 二进制搜索的最基本和最基本的形式
- 可以在不与元素的邻居（或使用其周围的特定元素）进行比较的情况下确定搜索条件
- 不需要进行后期处理，因为在每个步骤中，您都要检查是否已找到该元素。如果达到循环终止，那么您就知道找不到该元素
 

区分语法：

- 初始条件： ```left = 0, right = length-1```
- 终止： ```left > right```
- 向左搜索： ```right = mid-1```
- 正确搜索： ```left = mid+1```

### sqrt()
```py
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1
```

