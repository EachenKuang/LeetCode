# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 限制：
#
# 0 <= 链表长度 <= 1000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
from SwordOffer.DataStruct import ListNode, init_list_node_from_list, print_list_node


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        时间复杂度 O(M+N)
        空间复杂度 O(1)
        """
        result = ListNode(0)
        tmp = result
        curr_1, curr_2 = l1, l2
        while curr_1 and curr_2:
            if curr_1.val <= curr_2.val:
                tmp.next = ListNode(curr_1.val)
                curr_1 = curr_1.next

            else:
                tmp.next = ListNode(curr_2.val)
                curr_2 = curr_2.next
            tmp = tmp.next
        if curr_1:
            tmp.next = curr_1
        if curr_2:
            tmp.next = curr_2
        return result.next

    def mergeTwoLists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        缩减版
        """
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next


if __name__ == '__main__':
    solution = Solution()
    l1 = [1, 3, 4, 6, 7]
    l2 = [1, 3, 4]
    print_list_node(solution.mergeTwoLists(init_list_node_from_list(l1), init_list_node_from_list(l2)))
