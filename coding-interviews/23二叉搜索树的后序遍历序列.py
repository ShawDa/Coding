# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        mid, i = sequence[-1], 0
        for i in range(len(sequence)):
            if sequence[i] > mid:
                break
        for j in range(i, len(sequence)):
            if sequence[j] < mid:
                return False
        left, right = True, True
        if i > 2:
            left = self.VerifySquenceOfBST(sequence[:i])
        if left and len(sequence)-i > 3:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
