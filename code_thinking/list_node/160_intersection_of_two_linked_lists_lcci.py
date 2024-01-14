# -*- coding: utf-8 -*-
# @Time    : 2024/1/14 10:27
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 160_intersection_of_two_linked_lists_lcci.py
# https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from code_thinking.data_struct import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        常规双指针
        """
        # 2 交叉法
        # AAA  BB
        # AAABB
        # BBAAA
        # 这样两个链表的长度就一致了，那么如果，两个链表有交叉，那么最后一定有交叉，循环会终止在第一个节点
        # 如果两个链表没有交叉，那么最后循环会终止在最后一个None上。
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
        return pa
