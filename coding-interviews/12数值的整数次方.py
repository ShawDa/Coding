# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1 / base
        if exponent % 2 == 0:
            return self.Power(base, exponent//2) * self.Power(base, exponent//2)
        else:
            return self.Power(base, exponent//2) * self.Power(base, exponent//2 + 1)

    def Power1(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        res, e = 1, abs(exponent)
        while e > 0:
            if e & 1 == 1:
                res = res * base
            base = base * base
            e = e >> 1
        return res if exponent > 0 else 1 / res
