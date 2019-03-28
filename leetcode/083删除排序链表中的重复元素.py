# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head
        node = head
        while node and node.next:
            if node.val != node.next.val:
                node = node.next
            else:
                node.next = node.next.next
        return head
