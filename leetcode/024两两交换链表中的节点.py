# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        node = res
        while node.next and node.next.next:
            tmp1, tmp2 = node.next, node.next.next
            tmp1.next = tmp2.next
            node.next = tmp2
            tmp2.next = tmp1
            node = tmp1  # tmp1和tmp2已经交换
        return res.next
