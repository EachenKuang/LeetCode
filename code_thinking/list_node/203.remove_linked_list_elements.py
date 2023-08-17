# -*- coding: utf-8 -*-
# @Time    : 2023/8/17 21:59
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 203.remove_linked_list_elements.py
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# https://leetcode.cn/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from code_thinking.data_struct import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        带虚拟头节点的链表
        * 时间复杂度 O(n)
        * 空间复杂度 O(1)
        """
        dummy_head = ListNode(0)  # 使用一个虚拟头节点，可以解决需要处理头节点的问题，后续都建议如此操作
        dummy_head.next = head
        cur = dummy_head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next

    def removeElements_2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        不带虚拟头节点的链表
        * 时间复杂度 O(n)
        * 空间复杂度 O(1)
        """
        # 需要解决头节点需要删除的情况
        while head is not None and head.val == val:
            head = head.next

        pre = head
        cur = head.next
        while cur is not None:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head
