# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        list_x = list(reversed(list(str(x))))
        str_x = ''.join(list_x)
        if str_x.endswith('-'):
            str_x = '-' + str_x[:-1]
        if int(str_x) >= - 2**31 and int(str_x) <= 2**31 -1:
            return int(str_x)
        return 0

    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)[::-1]
        if str_x.endswith('-'):
            str_x = '-' + str_x[:-1]
        if int(str_x) >= - 2**31 and int(str_x) <= 2**31 -1:
            return int(str_x)
        return 0
