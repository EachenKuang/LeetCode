# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 使用两个指针（快慢）进行
        if not head or not head.next:
            return None
        q1 = head
        q2 = head.next
        while q1!= q2:
            if not q2 or not q2.next:
                return None
            q1 = q1.next
            q2 = q2.next.next
        # 确定有环，从头指针与q1 q2相遇的地方分别遍历
        res = head
        q1 = q1.next
        while res!=q1:
            res=res.next
            q1=q1.next
        return res
            