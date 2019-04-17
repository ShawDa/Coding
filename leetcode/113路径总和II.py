# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.sum = sum
        if not root:
            return self.res
        self.get_path(root,[root.val])
        return self.res

    def get_path(self, node, arr):
        if not node.left and not node.right and sum(arr) == self.sum:
            self.res.append(arr)
        if node.left:
            self.get_path(node.left, arr+[node.left.val])
        if node.right:
            self.get_path(node.right, arr+[node.right.val])

    def pathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        if not root:
            return self.res
        self.get_path1(root, [root.val], sum-root.val)
        return self.res

    def get_path1(self, node, arr, num):
        if not node.left and not node.right and num == 0:
            self.res.append(arr)
        if node.left:
            self.get_path1(node.left, arr+[node.left.val], num-node.left.val)
        if node.right:
            self.get_path1(node.right, arr+[node.right.val], num-node.right.val)
