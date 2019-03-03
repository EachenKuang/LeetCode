# https://leetcode.com/problems/sort-list/
"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
# 归并排序
class Solution1(object):
	 def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # find middle point 
        prev, fast, slow = None, head, head 
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        return self.merge(self.sortList(head),self.sortList(slow))
        # equal to 
        # return self.merge(*map(self.sortList,(head,slow)))
    def merge(self,headA,headB):
        dummy = tail = ListNode(None)
        while headA and headB:
            if headA.val > headB.val:
                tail.next = headB
                tail = headB
                headB = headB.next
            else:
                tail.next = headA
                tail = headA
                headA = headA.next
        tail.next = headA or headB
        return dummy.next
# a little cheated
class Solution2:
    def sortList(self, head: 'ListNode') -> 'ListNode':
        x=[];
        temp=head;
        while(head != None):
            x.append(head.val);
            head=head.next;
        x.sort();
        head =temp;
        for i in x:
            temp.val=i;
            temp=temp.next;
        return head;