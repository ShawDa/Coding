# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        x1, x2 = 1, 2
        while n >= 3:
            tmp = x2
            x2 = x1+x2
            x1 = tmp
            n -= 1
        return x2
