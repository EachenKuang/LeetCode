# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
# 找出数组之中三数相乘最大积
class Solution:
    # 1 常规策略
    # 一、至少有一个正数的情况下：
    # Step1：寻找最大整数
    # Step2：找剩下的两个最大正数和两个最小负数
    # Step3: 比较两大正与两小负数的乘积大小
    # 二、全是负数的情况下：
    # 实质上和上面的情况是一样的
    # 综合：
    # 找最大的三个数 m1,m2,m3，最小的两个数n1,n2
    # return max(m1*m2*m3,m1*n1*n2)
    
    # 1 常规排序  O(nlogn)
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])

    # 2 使用内置堆排序  O(nlogn)
    # heapq.nlargest(n, nums)
    def maximumProduct(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0]*a[1]*a[2], b[0]*b[1]*a[0])
    
    # 3 遍历数组法 O(n)
    def maximumProduct(self, nums):
        min1 = min2 = 1000
        max1 = max2 = max3 = -1000

        for num in nums:
            if num < min1:
                min1,min2 = num, min1
            elif num < min2:
                min2 = num
    
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
    
        return max(min1*min2*max1,  max1*max2*max3)