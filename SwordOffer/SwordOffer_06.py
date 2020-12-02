# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
#
# 示例 1：
#
# 输入：head = [1,3,2]
# 输出：[2,3,1]
#
# 限制：
#
# 0 <= 链表长度 <= 10000
#
# 链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
from typing import List

from SwordOffer.DataStruct import ListNode, init_list_node_from_list


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        temp_head = head
        reversed_list = []
        while temp_head:
            reversed_list.insert(0, temp_head.val)
            temp_head = temp_head.next
        return reversed_list

    def reversePrint2(self, head: ListNode) -> List[int]:
        """
        从头到尾，调换指针
        """
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        result = []
        while rev:
            result.append(rev.val)
            rev = rev.next
        return result


if __name__ == '__main__':
    solution = Solution()
    a_list = [1, 3, 4, 6, 7]
    input_items = init_list_node_from_list(a_list)
    print(solution.reversePrint(input_items))
    a_list.reverse()
    print(a_list)
    assert solution.reversePrint(input_items) == a_list
