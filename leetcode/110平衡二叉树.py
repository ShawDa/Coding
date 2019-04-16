# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [root]
        while stack:
            for i in range(len(stack)):
                treenode = stack.pop(0)
                left, right = treenode.left, treenode.right
                if abs(self.maxdepth(left) - self.maxdepth(right)) > 1:
                    return False
                else:
                    if left:
                        stack.append(left)
                    if right:
                        stack.append(right)
        return True

    def maxdepth(self, node):
        if not node:
            return 0
        return 1 + max(self.maxdepth(node.left), self.maxdepth(node.right))

    def isBalanced1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_depth = self.maxdepth1(root.left)
        right_depth = self.maxdepth1(root.right)
        if abs(left_depth-right_depth)>1:
            return False
        return self.isBalanced1(root.left) and self.isBalanced1(root.right)

    def maxdepth1(self, node):
        if not node:
            return 0
        return 1+max(self.maxdepth1(node.left), self.maxdepth1(node.right))
