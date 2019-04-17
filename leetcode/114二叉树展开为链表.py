# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        # 先把左右展开,在把右放到左最后,再把左放右,最后左置空
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            left, right = root.left, root.right
            while left.right:
                left = left.right
            left.right = right
            root.right = root.left
            root.left = None
