# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 1
        stack = [root.left, root.right]
        while stack:
            for i in range(len(stack)//2):
                node1, node2 = stack.pop(0), stack.pop(0)
                if node1 and node2:
                    stack.extend([node1.left, node1.right, node2.left, node2.right])
                elif node1:
                    stack.extend([node1.left, node1.right])
                elif node2:
                    stack.extend([node2.left, node2.right])
                else:
                    return depth
            depth += 1

    def minDepth1(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left and root.right:
            return 1 + min(self.minDepth1(root.left), self.minDepth1(root.right))
        else:
            return 1 + self.minDepth1(root.left) + self.minDepth1(root.right)
