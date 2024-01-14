# -*- coding: utf-8 -*-
# @Time    : 2024/1/13 10:50
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 206_revers_linked_list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from code_thinking.data_struct import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        双指针法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归法1 从前往后翻
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        return self.reverse(head, None)

    def reverse(self, cur: ListNode, pre: Optional[ListNode]) -> Optional[ListNode]:
        if cur is None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)

    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归法2 从后往前翻转
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        # 边缘判断
        if head is None or head.next is None:
            return head
        # 递归调用 第二个节点
        last = self.reverseList3(head.next)
        # 翻转操作
        head.next.next = head
        head.next = None

        return last

