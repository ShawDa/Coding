# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''
        if s:
            for one in s:
                if one.isalnum():
                    res += one
            res = res.lower()
        return res == res[::-1]
