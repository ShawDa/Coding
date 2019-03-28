# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = ListNode(head.val-1)
        res.next = head
        p, q = res, res.next
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
