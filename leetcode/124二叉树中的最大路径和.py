# -*- coding:utf-8 -*-
__author__ = 'ShawDa'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 二叉树中某一个节点为根结点的最大路径和,等于该节点的节点值,加上左子树的最大路径和
        # 加上右子树的最大路径和,若子树最大路径和为负,直接取0,不要这个子树
        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0
        left = max(0, self.helper(node.left))
        right = max(0, self.helper(node.right))
        self.res = max(self.res, node.val+left+right)
        # 返回左右子树中较大的那个作为父节点的一条路径
        return max(node.val+max(left, right), node.val)
