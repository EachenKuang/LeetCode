# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        root, tail, head = head, head, head.next
        while head:
            if head.val != tail.val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None

        return root
