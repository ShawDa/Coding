# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        res = []
        if not pRoot:
            return res
        stack= [pRoot]
        while stack:
            ceng = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                ceng.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(ceng)
        return res
