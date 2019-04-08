# https://leetcode.com/problems/merge-k-sorted-lists/
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 思路一：
# 先使用一个池子（长度为k）来保存当前的每个链表的第一个值，将池子中的最小值
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        import heapq
        def gen(node):
            while node:
                yield node.val, node
                node = node.next
        dummy = last = ListNode(None)
        for _, last.next in heapq.merge(*map(gen, lists)):
            last = last.next
        return dummy.next

