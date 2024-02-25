# -*- coding: utf-8 -*-
# @Time    : 2023/8/17 22:14
# @Author  : eachenkuang
# @Email   : eachen.kuang@foxmail.com
# @File    : data_struct.py
from typing import Optional


class ListNode:
    """ListNode"""
    def __init__(self, x: int = 0):
        self.val = x
        self.next = None


class TreeNode:
    """TreeNode"""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
