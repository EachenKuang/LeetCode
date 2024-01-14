# -*- coding: utf-8 -*-
# @Time    : 2024/1/14 11:00
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 19_remove_nth_node_from_end_of_list.py
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from code_thinking.data_struct import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        快慢指针法
        """
        # 使用虚拟头节点
        dummy_node = ListNode(0)
        dummy_node.next = head
        fast = dummy_node
        slow = dummy_node
        for i in range(n+1):
            if fast:
                fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_node.next
