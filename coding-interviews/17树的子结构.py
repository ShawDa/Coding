# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.same_root(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2)\
               or self.HasSubtree(pRoot1.right, pRoot2)

    def same_root(self, left, right):
        if not right:
            return True
        if not left or left.val != right.val:
            return False
        return self.same_root(left.left, right.left) and\
               self.same_root(left.right, right.right)
