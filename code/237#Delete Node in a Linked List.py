# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 这题有问题啊！要删除的点也没有，肯定是错了
        node.val = node.next.val
        node.next = node.next.next
    # 上面的代码可以通过，且beat100%

    # 实际上我认为题目应该是这样
    def deleteNode(self, head,node):
        """
        :type head: ListNode
        :type node: int
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while head and head.next:
            if head.val==node:
                head = head.next
                return
