# https://leetcode.com/problems/linked-list-cycle/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 使用两个指针（快慢）进行
        if not head or not head.next:
            return False
        q1 = head
        q2 = head.next
        while q1!= q2:
            if not q2 or not q2.next:
                return False
            q1 = q1.next
            q2 = q2.next.next
        return True