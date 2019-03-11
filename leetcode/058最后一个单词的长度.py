# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = s.split()
        return len(list_s[-1]) if list_s else 0
