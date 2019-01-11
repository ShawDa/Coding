# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0:
            return str(bin(n)).count('1')
        else:
            return str(bin(2**32+n)).count('1')

    def NumberOf1_1(self, n):
        # write code here
        count = 0
        flag = 1
        while flag < 2**32:
            if n & flag != 0:
                count += 1
            flag = flag << 1
        return count

    def NumberOf1_2(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            n = n & (n-1)
            count += 1
        return count
