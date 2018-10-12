# https://leetcode.com/problems/remove-linked-list-elements/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ret = res = ListNode(0)
        res.next = head
        while res.next:
            if res.next.val==val:
                res.next = res.next.next
            else:
                res = res.next        
        return ret.next