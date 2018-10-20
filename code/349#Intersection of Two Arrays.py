# https://leetcode.com/problems/intersection-of-two-arrays/description/
class Solution:
    # 1 使用set集合以及函数intersection
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))
        # list(set(nums1)&set(nums2)) 同样可以
    # 2 常规方法
    # 先排序，然后遍历
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ret = set()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ret.add(nums1[i])
                i += 1
                j += 1
        return list(ret)