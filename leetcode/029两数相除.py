# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 不能用除法，那就只能用减法咯～首先想到的是一次一次的减，这样就太慢了，
        # 所以最后以指数递增的方式做减法，直到被除数小于除数才停止。注意要先判断符号，然后再对两个正数相除
        MAX_INT, MIN_INT = 2**31-1, -2**31
        sign = -1 if min(dividend, divisor) < 0 and max(dividend, divisor) > 0 else 1
        up, down = abs(dividend), abs(divisor)
        res = self.divide_positive(up, down)
        if sign == -1:
            res = -res
        if res > MAX_INT or res < MIN_INT:
            return MAX_INT
        return res

    def divide_positive(self, up ,down):
        res, tmp, i = 0, down, 1
        while up >= tmp:
            res += i
            up -= tmp
            tmp = 2* tmp
            i = 2*i
        if up >= down:
            res += self.divide_positive(up, down)
        return res
