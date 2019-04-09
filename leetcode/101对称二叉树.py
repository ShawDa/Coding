# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #  递归
        return self.isMirror(root, root)

    def isMirror(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        return (root1.val == root2.val and self.isMirror(root1.left, root2.right)
                and self.isMirror(root1.right, root2.left))

    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 迭代 用列表模拟一个栈 每次把一边的左子树和一边的右子树压进去
        stack = [root, root]
        while stack:
            root1 = stack.pop()
            root2 = stack.pop()
            if root1 == None and root2 == None:
                continue
            if root1 == None or root2 == None:
                return False
            if root1.val != root2.val:
                return False
            stack.extend([root1.left, root2.right, root1.right, root2.left])
        return True
