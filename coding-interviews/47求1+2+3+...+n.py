# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def Sum_Solution(self, n):
        # write code here
        res = n
        left = res and self.Sum_Solution(n-1)  # 到0停止
        res += left
        return res
