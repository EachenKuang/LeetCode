# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 限制：
#
# 0 <= 节点个数 <= 5000
#
# 链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
from SwordOffer.DataStruct import ListNode, init_list_node_from_list, print_list_node


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        使用额外空间，不改变原有的链表
        """
        first = head
        res = []
        while first:
            res.insert(0, first.val)
            first = first.next
        return init_list_node_from_list(res)

    def reverseList_2(self, head: ListNode) -> ListNode:
        prev, curr = ListNode(0), head
        while curr:
            tmp = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = tmp
        return prev.next


if __name__ == '__main__':
    solution = Solution()
    test_suits = [
        [1, 3, 4, 6, 7],
        [1, 3, 4],
        [1],
        [2, 4]
    ]
    for test_suit in test_suits:
        input_items = init_list_node_from_list(test_suit)
        print_list_node(solution.reverseList(input_items))

    for test_suit in test_suits:
        input_items = init_list_node_from_list(test_suit)
        print_list_node(solution.reverseList_2(input_items))
