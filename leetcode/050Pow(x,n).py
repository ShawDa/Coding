# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        abs_n = abs(n)
        res = 1
        while abs_n > 0:
            if abs_n & 1:
                res = res * x
            x = x * x
            abs_n = abs_n >> 1
        return res if n > 0 else 1 / res
