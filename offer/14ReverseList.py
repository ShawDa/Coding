# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 输入一个链表，反转链表后，输出新链表的表头。  就是反转链表
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        head = None
        while pHead:
            tmp = pHead.next  # 暂存下一位
            pHead.next = head
            head = pHead
            pHead = tmp  # 取下一位
        return head
