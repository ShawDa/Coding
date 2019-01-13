# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # 递归
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2

    def Merge1(self, pHead1, pHead2):
        # write code here
        # 非递归
        res = ListNode(1)
        head = res
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                res.next = pHead1
                pHead1 = pHead1.next
            else:
                res.next = pHead2
                pHead2 = pHead2.next
            res = res.next
        if pHead1:
            res.next = pHead1
        if pHead2:
            res.next = pHead2
        return head.next
