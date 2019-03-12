# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        len_listnode, node = 0, head
        while node:
            len_listnode += 1
            node = node.next
        cut_length = len_listnode - (k % len_listnode)
        if cut_length == 0 or cut_length == len_listnode:
            return head
        node = head
        for i in range(cut_length-1):
            node = node.next
        tmp = node.next
        node.next = None
        after = tmp
        while after.next:
            after = after.next
        after.next = head
        return tmp

    def rotateRight1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        len_listnode, node = 1, head
        while node.next:
            len_listnode += 1
            node = node.next
        node.next = head  # 先连成环,然后再切
        for i in range(len_listnode-k % len_listnode):
            node = node.next
        res = node.next
        node.next = None
        return res
