# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        res = ListNode(0)
        while pHead:
            tmp = pHead.next
            pHead.next = res.next
            res.next = pHead
            pHead = tmp
        return res.next
