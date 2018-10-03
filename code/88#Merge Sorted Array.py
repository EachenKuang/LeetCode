# https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    # 1 normal function
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # use 2 point in nums1 and nums2
        point1 = m-1
        point2 = n-1
        insert_point = m+n-1
        while nums2 and point1>=0:
            if nums2[point2] >=nums1[point1]:
                nums1[insert_point] = nums2.pop()
                point2 -=1
            else:
                nums1[insert_point] = nums1[point1]
                nums1[point1] = 0
                point1 -=1
            insert_point -=1
        while nums2:
            nums1[insert_point] = nums2.pop()
            point2 -=1
            insert_point -=1
    # 2 two line function
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # use 2 point in nums1 and nums2
        nums1[m:] = nums2[:n]
        nums1.sort()
    # 3
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]