# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        list_n, start = list(range(n)), 0
        while len(list_n) > 1:
            loc = (start + m -1) % len(list_n)  # 移除点位置
            list_n.pop(loc)
            if loc == len(list_n):
                start = 0
            else:
                start = loc
        return list_n[0]

