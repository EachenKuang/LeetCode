# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 1 使用双指针
        # 先用p,q两个指针同时从两个链表遍历，当遍历到任意一个就停止。
        # 假设A,B的长度为a,b且a>=b；那么两个链表相差a-b的长度。
        # 如果两个链表相交，那么当A链表先走a-b的长度，然后两个链表同时走
        # 一定可以同时到达链表尾部
        if not headA or not headB:
            return None
        p = headA
        q = headB
        while p and q:
            p = p.next
            q = q.next
        if p:
            # A链表长
            temp = headA
            while p:
                p = p.next
                temp = temp.next
            p = headA
            q = headA
        elif q:
            # B链表长
            temp = headB
            while q:
                q = q.next
                temp = temp.next
            p = headA
            q = temp
        else:
            # 两链表同长
            p = headA
            q = headB
        
        while p!=q:
            p = p.next
            q = q.next
        return p


        # 2 交叉法
        # AAA  BB
        # AAABB
        # BBAAA
        # 这样两个链表的长度就一致了，那么如果，两个链表有交叉，那么最后一定有交叉，循环会终止在第一个节点
        # 如果两个链表没有交叉，那么最后循环会终止在最后一个None上。
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA

        return pa