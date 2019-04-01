# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        before = res  # 反转的前一个节点
        for i in range(m-1):
            before = before.next
        a = before.next
        b = a.next
        while m < n:  # 把b放到翻转的最前面
            a.next = b.next
            b.next = before.next
            before.next = b
            b = a.next
            m += 1
        return res.next
