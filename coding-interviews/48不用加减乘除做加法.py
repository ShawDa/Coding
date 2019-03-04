# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:  # 直到进位和为0
            tmp = num1^num2  # 不算进位的和
            num2 = (num1&num2)<<1  # 进位的和
            num1 = tmp
        return num1

    def Add1(self, num1, num2):
        # write code here
        return sum([num1, num2])
