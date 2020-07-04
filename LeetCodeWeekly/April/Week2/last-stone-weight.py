# We have a collection of stones, each stone has a positive integer weight.
#
# Each turn, we choose the two heaviest stones and smash them together.
# Suppose the stones have weights x and y with x <= y.  The result of this smash is:
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
#
#
#
# Example 1:
#
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
#
#
# Note:
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

# 这里涉及到排名前二的数组，可以使用堆排序来完成
# 先建堆，然后去掉前二，然后插入堆中，循环到最后
import heapq


class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]

        max_heap = []

        # add to heap
        for ele in stones:
            heapq.heappush(max_heap, -ele)
            # 这里是一种非常trick的方法，因为Python中默认是使用小顶堆，不支持通过反转方式初始化大顶堆
            # 这里插入取负的值，需要注意的是在最后需要取回正

        # loop until len(heap) <= 1
        while len(max_heap) >= 2:
            y = -heapq.heappop(max_heap)  # largest
            x = -heapq.heappop(max_heap)  # 2nd largest

            if x == y:
                continue
            else:
                heapq.heappush(max_heap, - (y - x))

        if len(max_heap) == 0:
            return 0
        else:  # only one stone is left in max_heap
            return -max_heap[0]


class Solution1:
    def lastStoneWeight(self, stones: [int]):
        while len(stones) >= 2:
            stones.sort()  # 因为数组的数量在30以内，所以这里的时间复杂度还是O(1)
            largest = stones.pop()
            second_largest = stones.pop()
            stones.append(largest - second_largest)  # 相同相当于增加0这个数
        if stones:
            return stones[0]
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastStoneWeight([2,7,4,1,8,1]))