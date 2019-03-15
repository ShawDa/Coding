# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return None
        slow, fast = pHead.next, pHead.next.next  # 走一步和两步
        while slow != fast:
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
        res = pHead
        while res != slow:
            res = res.next
            slow = slow.next
        return res
