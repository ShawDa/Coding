# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = ListNode(0), ListNode(0)
        node1, node2 = left, right
        while head:
            if head.val < x:
                node1.next = head
                head = head.next  # 注意要在这里加,若最后加就为空
                node1 = node1.next
                node1.next = None
            else:
                node2.next = head
                head = head.next
                node2 = node2.next
                node2.next = None
        node1.next = right.next
        return left.next
