# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + \
               [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack:
            if root:  # 如果当前节点不为空则进栈,并移动到左孩子
                stack.append(root)
                root = root.left
            else:  # 走到最左端了,移动到右孩子
                root = stack.pop(-1)
                res.append(root.val)
                root = root.right
        return res
