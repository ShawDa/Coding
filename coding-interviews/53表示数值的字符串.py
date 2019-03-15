# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    # s字符串
    def isNumeric(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
