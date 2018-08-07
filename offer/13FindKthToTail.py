# -*- coding:utf-8 -*-


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 输入一个链表，输出该链表中倒数第k个结点。  返回节点
    def FindKthToTail(self, head, k):
        # write code here 两个指针p1 p2，一个先走k-1，第二个开始走，第一个走到尾第二个就算倒数第k个
        if head == None or k <=0:
            return None
        p1, p2 = head, head
        while k > 1:
            if p1.next != None:
                p1 = p1.next
                k -= 1
            else:
                return None
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        return p2
