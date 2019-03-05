# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def StrToInt(self, s):
        # write code here
        # 先看是否为空，再判断首位是否有符号，最后看每一位是否是数字
        if len(s) == 0:
            return 0
        flag = -1 if s[0] == '-' else 1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        res = 0
        for i, num in enumerate(s):
            if '0' <= num <= '9':
                res = 10 * res + int(num)
            else:
                return 0
        return res * flag
