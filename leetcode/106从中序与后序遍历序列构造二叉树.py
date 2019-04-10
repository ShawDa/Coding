# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # inorder = [9, 3, 15, 20, 7],postorder = [9, 15, 7, 20, 3]
        if not inorder:
            return None
        res = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        res.left = self.buildTree(inorder[:index], postorder[:index])
        res.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return res
