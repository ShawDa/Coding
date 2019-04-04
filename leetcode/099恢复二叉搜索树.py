# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.tmp, self.left, self.right = None, None, None
        self.helper(root)
        self.left.val, self.right.val = self.right.val, self.left.val

    def helper(self, node):
        # 示例-1,5,2,3,1,7 第一次左大于右选左 最后一次左大于右选右
        if not node:
            return
        # 中序遍历,左中右
        self.helper(node.left)
        if self.tmp and self.tmp.val > node.val:
            if not self.left:
                self.left = self.tmp
            self.right = node
        self.tmp = node  # 指向前一个节点
        self.helper(node.right)
