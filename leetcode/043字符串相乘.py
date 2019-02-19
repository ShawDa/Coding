# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        for i, a in enumerate(num1[::-1]):
            for j, b in enumerate(num2[::-1]):
                one = int(a) * int(b)
                one += res[i+j]
                res[i+j+1] += one // 10
                res[i+j] = one % 10
        res.reverse()
        res = ''.join(map(str, res))
        while res.startswith('0'):
            res = res[1:]
        return res
