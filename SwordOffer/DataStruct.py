from collections import deque
from typing import List, Union


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


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
    print(init_list_from_list_node(list_node))


def list_to_binary_tree(nums: List) -> Union[TreeNode, None]:
    if not nums:
        return None
    iter_value = iter(nums)
    root = TreeNode(next(iter_value))
    d = deque()
    d.append(root)
    while 1:
        head = d.popleft()
        try:
            head.left = TreeNode(next(iter_value))
            d.append(head.l_node)
            head.right = TreeNode(next(iter_value))
            d.append(head.r_node)
        except StopIteration:
            break
    return root


def list_to_binary_tree_2(nums: List) -> Union[TreeNode, None]:
    def level(index):
        if index >= len(nums):
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


def tree_to_list(tree: TreeNode) -> List:
    """
    TODO: 完成转化函数以及测试用例
    """
    if not tree:
        return []


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6]
    test_list_node = init_list_node_from_list(test_list)
    assert test_list == init_list_from_list_node(test_list_node)
    print_list_node(test_list_node)
