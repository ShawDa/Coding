# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        return 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))

    def TreeDepth1(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        queue, height = [pRoot], 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height += 1
        return height
