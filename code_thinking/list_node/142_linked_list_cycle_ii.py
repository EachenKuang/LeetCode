# -*- coding: utf-8 -*-
# @Time    : 2024/1/14 10:45
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 142_linked_list_cycle_ii.py
# https://leetcode.cn/problems/linked-list-cycle-ii/
from typing import Optional

from code_thinking.data_struct import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        快慢指针法
        """
        fast = head  # 快指针
        slow = head  # 慢指针
        # fast每次走两步，需要保证 fast 以及 fast.next 不为空
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 如果存在环，则快慢指针必会相遇
            if slow == fast:
                temp1 = head
                temp2 = slow
                # 从相遇点，以及链表起点，分别出发，相遇点就是入口
                while temp1 != temp2:
                    temp1 = temp1.next
                    temp2 = temp2.next
                return temp1
        return None

    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        集合法 需要保存访问过的节点
        """
        visited = set()

        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None