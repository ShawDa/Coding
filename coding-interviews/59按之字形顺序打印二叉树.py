# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        res = []
        if not pRoot:
            return res
        stack, flag = [pRoot], 1
        while stack:
            ceng = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                ceng.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if flag == -1:
                ceng.reverse()
            flag *= -1
            res.append(ceng)
        return res
