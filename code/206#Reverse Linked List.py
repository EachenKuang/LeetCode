# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	# 迭代法
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = None
        point = head
        while point:
            nextTemp = point.next;
            point.next = root;
            root = point;
            point = nextTemp;
        return root
    # 递归法
    def reverseList(self, head):
    	"""
    	:type head: ListNode
    	:rtype: ListNode
    	"""
    	if not head:
    		return head
    	return reverse_res(head)

    	def reverse_res(head):
    		if head.next == None:
               	return head
           	temp = reverse_res(head.next)
        	head.next.next = head
        	head.next = null
        	return temp