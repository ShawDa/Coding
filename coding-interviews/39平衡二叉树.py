# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return abs(self.tree_height(pRoot.left) - self.tree_height(pRoot.right)) <= 1 and \
               self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def tree_height(self, node):
        if not node:
            return 0
        return 1 + max(self.tree_height(node.left), self.tree_height(node.right))

    def IsBalanced_Solution1(self, pRoot):
        # write code here
        return self.tree_height1(pRoot) != -1

    def tree_height1(self, node):
        if not node:
            return 0
        left = self.tree_height(node.left)
        if left == -1:  # 每次都判断下是否平衡
            return -1
        right = self.tree_height(node.right)
        if right == -1:
            return -1
        # 最后再判断下是否平衡，如果平衡就返回该节点高度
        return -1 if abs(left-right) > 1 else 1+max(left, right)
