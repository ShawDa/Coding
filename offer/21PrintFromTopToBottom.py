# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    # 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
    def PrintFromTopToBottom(self, root):  # 层序遍历 模拟队列
        # write code here
        if root == None:
            return []
        queue = [root]
        result = []
        while queue:
            newqueue = []
            for one in queue:
                if one.left != None:
                    newqueue.append(one.left)
                if one.right != None:
                    newqueue.append(one.right)
                result.append(one.val)
            queue = newqueue
        return result
