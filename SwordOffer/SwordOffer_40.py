# https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

# 示例 1：

# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
# 示例 2：

# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#  

# 限制：

# 0 <= k <= arr.length <= 10000
# 0 <= arr[i] <= 10000

from typing import List


class Solution:
    """
    方法一：
    先排序，然后取前面K个   
    时间复杂度 与排序有关  O(nlogn)
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
    """
    方法二：
    堆排序，获取前K个最小值，使用小顶堆
    建堆 O(N)+O(klogN)
    """
    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
    """
    方法三：
    冒泡排序，做k次冒泡，最后的K的就是
    时间复杂度 O(KN)
    """