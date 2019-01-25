# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur, check, count, cnt = head, head, 0, 0
        while count < k and check:
            check = check.next
            count += 1
        if count == k:
            prev, next_node = None, None
            for i in range(k):  # 翻转
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            if next_node:
                # head为翻转后尾节点
                head.next = self.reverseKGroup(next_node, k)
            return prev  # prev为翻转后头结点
        else:
            return head

    def reverseKGroup1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node, count = head, 0
        while count < k and node:
            count += 1
            node = node.next
        if count == k:
            node = self.reverseKGroup(node, k)  # 将后面的翻转好作为后续
            while count > 0:  # 翻转
                tmp = head.next
                head.next = node
                node = head
                head = tmp
                count -= 1
            head = node  # 最后把头结点赋给head
        return head
