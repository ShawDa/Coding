# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        res = []
        if start > end:
            return [None]
        for i in range(start, end+1):  # 找个根节点
            left = self.helper(start,i-1)
            right = self.helper(i+1, end)
            for one_left in left:
                for one_right in right:
                    # 从左右各找一个节点作为左右子树的根节点
                    node = TreeNode(i)
                    node.left = one_left
                    node.right = one_right
                    res.append(node)
        return res
