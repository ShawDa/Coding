# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except ValueError:
            return False
