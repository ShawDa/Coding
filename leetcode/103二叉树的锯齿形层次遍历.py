# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        flag = 1
        res = []
        stack = [root]
        while stack:
            res0 = []
            for i in range(len(stack)):
                node = stack.pop(0)
                if node:
                    stack.extend([node.left, node.right])
                    res0.append(node.val)
            if flag == 1:
                flag = -1
            else:
                flag = 1
                res0.reverse()
            if res0:
                res.append(res0)
        return res
