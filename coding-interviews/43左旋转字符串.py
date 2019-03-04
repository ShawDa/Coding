# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:] + s[:n]

    def LeftRotateString1(self, s, n):
        # write code here
        x, y = s[:n], s[n:]
        x, y = x[::-1], y[::-1]
        return (x+y)[::-1]
