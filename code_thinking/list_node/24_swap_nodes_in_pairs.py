# -*- coding: utf-8 -*-
# @Time    : 2024/1/13 11:17
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : 24_swap_nodes_in_pairs.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
from typing import Optional

from code_thinking.data_struct import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        前后指针法
          +--------+         +-------+         +---------+       +---------+       +---------+
          |   cur  |  -----  |   1   |  -----  |    2    | ----- |    3    | ----- |    4    |
          +--------+         +-------+         +---------+       +---------+       +---------+
        """
        # 使用一个冗余指针指向头节点
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur = dummy_node
        while cur.next and cur.next.next:
            # 存储临时节点
            temp1 = cur.next  # 节点1
            temp2 = cur.next.next.next  # 节点3
            # 步骤1  cur 指向 节点 2
            cur.next = cur.next.next
            # 步骤2  节点2 指向 节点 1
            cur.next.next = temp1
            # 步骤3  节点1 指向 节点 3
            temp1.next = temp2
            cur = cur.next.next
        return dummy_node.next
