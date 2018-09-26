# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = l1 # 使用l1作为链表，不用创建新的链表
        while l1 or l2:
            l1.val += l2.val + carry if l2 else carry
            carry = l1.val//10 # 使用标准除法，如果大于等于10则carry置1
            l1.val %= 10
            if l2:
                l2=l2.next
            if l1.next:
                l1=l1.next
            elif carry or l2:
                l1.next=ListNode(0) #如果l1没有则补0
                l1=l1.next
            else:
                break
        return res
