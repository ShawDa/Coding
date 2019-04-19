# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        # 左子树的左子树和右子树的右子树比较,右子树的左子树和左子树的右子树比较
        if not pRoot:
            return True
        return self.symmetrical(pRoot.left, pRoot.right)

    def symmetrical(self, a, b):
        if not a:
            return not b
        return b and a.val == b.val and \
               self.symmetrical(a.left, b.right) and self.symmetrical(a.right, b.left)
