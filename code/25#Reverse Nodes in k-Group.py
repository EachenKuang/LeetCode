# https://leetcode.com/problems/reverse-nodes-in-k-group/
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        node, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return node

# 迭代
# Iteratively
def reverseKGroup(self, head, k):
    if not head or not head.next or k <= 1:
        return head
    cur, l = head, 0
    while cur:
        l += 1
        cur = cur.next
    if k > l:
        return head
    dummy = pre = ListNode(0)
    dummy.next = head
    # totally l//k groups
    for i in range(l//k):
        # reverse each group
        node = None
        for j in range(k-1):
            nxt = head.next
            head.next = node
            node = head
            head = nxt
        # update nodes and connect nodes
        tmp = head.next
        head.next = node
        pre.next.next = tmp
        tmp1 = pre.next
        pre.next = head
        head = tmp
        pre = tmp1
    return dummy.next
