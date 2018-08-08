# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回镜像树的根节点
    # 操作给定的二叉树，将其变换为源二叉树的镜像。
    """
    二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
    """
    def Mirror(self, root):
        # write code here 递归
        if root == None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
