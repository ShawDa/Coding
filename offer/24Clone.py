# -*- coding:utf-8 -*-

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None

        # 递归
        # newnode = RandomListNode(pHead.label)
        # newnode.random = pHead.random
        # newnode.next = self.Clone(pHead.next)
        # return newnode

        # 复制拆分
        dummy = pHead
        while dummy:  # 复制
            tmp = dummy.next
            newnode = RandomListNode(dummy.label)
            dummy.next = newnode
            newnode.next = tmp
            dummy = tmp

        dummy = pHead
        while dummy:  # 复制random
            random = dummy.random
            copynode = dummy.next
            if random:
                copynode.random = random
            dummy = copynode.next

        dummy = pHead
        copyhead = pHead.next  # 头
        while dummy:  # 取
            copynode = dummy.next
            dummynext = copynode.next
            dummy.next = dummynext
            if dummynext:
                copynode.next = dummynext.next
            else:
                copynode.next = None
            dummy = dummynext

        return copyhead
