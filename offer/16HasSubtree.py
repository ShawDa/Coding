# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        return self.aHasb(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        # 注意返回的第一个条件不是要求这两树相同，而是根节点相同，b为a的一部分

    def aHasb(self, a, b):  # 看从根节点开始，b是否为a的一部分或者相同
        if b == None:  # 如果遍历到b为空，对
            return True
        if a == None:  # 如果遍历到a为空，错
            return False
        if a.val != b.val:  # 如果有一个节点值不同，错
            return False
        return self.aHasb(a.left, b.left) and self.aHasb(a.right, b.right)
