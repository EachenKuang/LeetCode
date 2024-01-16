# -*- coding: utf-8 -*-
# @Time    : 2024/1/16 23:07
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 349_intersection_of_two_arrays.py
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        一行解决问题
        """
        return list(set(i for i in nums1 if i in nums2))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        一行解决问题，使用 set 的能力
        """
        return list(set(nums1).intersection(nums2))

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """常规写法"""
        res_set = set()
        for i in nums1:
            if i in nums2:
                res_set.add(i)
        return list(res_set)

    def intersection4(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
