# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        cur = res
        flag = 0
        while (l1 != None or l2!= None):
            if l1 != None:
                x = l1.val
            else:
                x = 0
            if l2 != None:
                y = l2.val
            else:
                y = 0
            sum_xy = flag + x + y
            flag = sum_xy // 10
            cur.next = ListNode(sum_xy%10)
            cur = cur.next
            if l1!= None:
                l1 = l1.next
            if l2!= None:
                l2 = l2.next
        if flag > 0 :
            cur.next = ListNode(flag)
        return res.next
