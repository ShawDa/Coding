# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        # 如果两链表长度相同,若有相同节点,则到尾部之前就可以找到;否则到最后返回None.
        # 如果两链表长度不同,长度分别为a+c和b+c,若有相同节点,则当两个点都走了a+b+c步时就找到了;
        # 否则最后都走a+b+2c步到最后返回None.
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1
