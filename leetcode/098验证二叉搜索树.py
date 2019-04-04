# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root)

    def helper(self, root, left=float('-inf'), right=float('inf')):
        if not root:
            return True
        # 每个节点都有个值的范围,约束一下就好
        return left < root.val < right and self.helper(root.left, left, root.val)\
               and self.helper(root.right, root.val, right)

    def isValidBST1(self, root: TreeNode) -> bool:
        return self.helper1(root)

    def helper1(self, root, left=None, right=None):
        if not root:
            return True
        if left and left.val >= root.val:
            return False
        if right and right.val <= root.val:
            return False
        return self.helper(root.left, left, root) and\
               self.helper(root.right, root, right)
