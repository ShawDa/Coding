# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list_x = list(str(x))
        if list_x == list(reversed(list_x)):
            return True
        else:
            return False

    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        half_num = 0
        while x > half_num:  # x有len(str(x))//2的长度
            half_num = half_num * 10 + x % 10
            x = x // 10
        return x == half_num or x == half_num // 10

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
