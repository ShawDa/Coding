# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        return self.helper(head, None)

    def helper(self, begin, end):  # 辅助函数,[begin:end]
        if begin == end:
            return None
        slow, fast = begin, begin
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        res = TreeNode(slow.val)
        res.left = self.helper(begin, slow)
        res.right = self.helper(slow.next, end)
        return res
