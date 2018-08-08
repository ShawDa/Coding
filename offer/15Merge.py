# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    # 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        head = ListNode(0)
        phead = head
        while pHead1 != None and pHead2 != None:
            if pHead1.val <= pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
            else:
                head.next = pHead2
                pHead2 = pHead2.next
            head = head.next
        if pHead1 != None:
            head.next = pHead1
        else:
            head.next = pHead2
        return phead.next

        """ 递归
        pMergedHead = None #设置新链表
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1, pHead2.next)
        return pMergedHead
        """


if __name__ == '__main__':
    s = Solution()
    phead1 = ListNode(1)
    phead2 = ListNode(2)
    phead1.next = ListNode(3)
    pheadx = phead1.next
    pheadx.next = ListNode(5)
    phead2.next = ListNode(4)
    pheady = phead2.next
    pheady.next = ListNode(6)
    print(phead1, phead2)
    print(phead1.next.val, phead2.next.val)
    print(s.Merge(phead1, phead2))
    pass
