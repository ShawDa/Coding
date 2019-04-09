# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        stack = [root.left, root.right]
        while stack:
            for i in range(len(stack)//2):
                node1, node2 = stack.pop(0), stack.pop(0)
                if node1:
                    stack.extend([node1.left, node1.right])
                if node2:
                    stack.extend([node2.left, node2.right])
            depth += 1
        return depth

    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
