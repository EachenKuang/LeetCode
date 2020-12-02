from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    
def init_list_node_from_list(list_node: List):
    ret_node_list = ListNode(0) 
    key = ret_node_list
    for node in list_node:
        key.next = ListNode(node)
        key = key.next
    return ret_node_list.next


def init_list_from_list_node(list_node: ListNode):
    ret_list = []
    head = list_node
    while head:
        ret_list.append(head.val)
        head = head.next
    return ret_list


def print_list_node(list_node: ListNode):
    head = list_node
    while head:
        print(head.val)
        head = head.next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6]
    test_list_node = init_list_node_from_list(test_list)
    assert test_list == init_list_from_list_node(test_list_node)
    print_list_node(test_list_node)
