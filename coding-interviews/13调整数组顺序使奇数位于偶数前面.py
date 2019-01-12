# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def reOrderArray(self, array):
        # write code here
        left, right = [], []
        for num in array:
            if num % 2 == 1:
                left.append(num)
            else:
                right.append(num)
        return left+right
