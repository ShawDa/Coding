# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def multiply(self, A):
        # write code here
        # 上三角 下三角
        if not A:
            return []
        length = len(A)
        res, tmp = [1]*length, 1
        for i in range(1, length):
            res[i] = res[i-1]*A[i-1]
        for j in range(length-2, -1, -1):
            tmp *= A[j+1]
            res[j] *= tmp
        return res
