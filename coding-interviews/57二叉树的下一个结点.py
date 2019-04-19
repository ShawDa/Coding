# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:  # 下一个节点一定在右子树的最左端
            res = pNode.right
            while res.left:
                res = res.left
            return res
        else:
            father = pNode.next
            while father and father.right == pNode:  # 如果节点是父节点的右儿子，那么继续往上
                pNode = father
                father = pNode.next
            return father
