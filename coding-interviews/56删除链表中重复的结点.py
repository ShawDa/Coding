# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        res = ListNode(pHead.val - 1)
        res.next = pHead
        p, q = res, pHead
        while q and q.next:
            if q.val != q.next.val:
                p = q
                q = q.next
            else:
                while q.next and q.val == q.next.val:
                    q = q.next
                q = q.next
                p.next = q
        return res.next

    def deleteDuplication1(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        if pHead.val != pHead.next.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:  # 如果相等那么找第一个不等的节点
            node = pHead.next
            while node and node.val == pHead.val:
                node = node.next
            return self.deleteDuplication(node)
        return pHead
