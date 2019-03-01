# https://leetcode.com/problems/partition-list/
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = pre = ListNode(0)
        big = post = ListNode(0)
        while head:
            if head.val < x:
                pre.next = head
                pre = pre.next
            else:
                post.next = head
                post = post.next
            head = head.next
        pre.next = big.next
        post.next = None
        return small.next
# Runtime: 44 ms, faster than 50.18% of Python3 online submissions for Partition List.
# Memory Usage: 13.4 MB, less than 6.12% of Python3 online submissions for Partition List.