# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        self.res, self.flag = None, None
        self.convert(pRootOfTree)
        return self.res

    def convert(self, root):
        if not root:
            return None
        self.convert(root.left)
        if self.res == None:
            self.res, self.flag = root, root
        else:
            self.flag.right = root
            root.left = self.flag
            self.flag = root
        self.convert(root.right)
