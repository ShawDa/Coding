# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]
        res = ''
        for i, j in enumerate([1000, 100, 10, 1]):
            res += romans[i][num//j]
            num = num % j
        return res

    def intToRoman1(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]
        return romans[0][num // 1000] + romans[1][num % 1000 // 100]\
               + romans[2][num % 100 // 10] + romans[3][num % 10]
