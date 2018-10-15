# https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 1 常规方法
    # 时间O(n),空间O(n)
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 常规方法：先将值存储起来，然后判断
        temp_list = []
        
        while head:
            temp_list.append(head.val)
            head=head.next
        l = len(temp_list)
        for i in range(0, l//2):
            if temp_list[i] != temp_list[l-1-i]:
                return False            
        return True
    # 2 反转链表成两个链表，进行判断
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        
        # 到达链表中间停止
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 将后半段的链表反转
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        # 两个链表比较
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
                
        
        return True


        