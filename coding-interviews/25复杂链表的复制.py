# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        res = RandomListNode(pHead.label)
        res.random = pHead.random
        res.next = self.Clone(pHead.next)
        return res

    def Clone1(self, pHead):
        # write code here
        if pHead == None:
            return None

        head = pHead
        while head:
            tmp = head.next
            head.next = RandomListNode(head.label)
            head.next.next = tmp
            head = tmp

        head = pHead
        while head:
            copy_node = head.next
            next_head = copy_node.next
            if head.random:
                copy_node.random = head.random.next
            head = next_head

        head = pHead
        res = pHead.next
        while head:
            copy_node = head.next
            next_head = copy_node.next
            head.next = next_head
            if next_head:
                copy_node.next = next_head.next
            else:
                copy_node.next = None
            head = next_head
        return res
