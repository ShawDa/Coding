# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        flag, res = 1, 0
        if str[0] == '-':
            flag, str = -1, str[1:]
        elif str[0] == '+':
            str = str[1:]
        for char in str:
            if '0' <= char <= '9':
                res = 10*res + int(char)
            else:
                break
        res = flag * res
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
