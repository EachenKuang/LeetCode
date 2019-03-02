# https://leetcode.com/problems/reverse-linked-list-ii/
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        tail, con = cur, prev

        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head