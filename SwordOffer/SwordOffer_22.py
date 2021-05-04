# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
#
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
#
#  
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
#
# 返回链表 4->5.
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
from SwordOffer.DataStruct import ListNode, init_list_node_from_list, print_list_node


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
        快慢指针法
        这里假设k一定小于链表的长度，如果k大于链表长度，则默认返回head
        以及如果head为空的情况下
        """
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == '__main__':
    solution = Solution()
    test_suits = [
        [1, 3, 4, 6, 7],
        [1, 3, 4],
        [1],
        [2, 4]
    ]
    k_list = [3, 1, 1, 2]
    for test_suit, k in zip(test_suits, k_list):
        input_items = init_list_node_from_list(test_suit)
        print_list_node(solution.getKthFromEnd(input_items, k))
