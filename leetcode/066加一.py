# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag, length = 0, len(digits)
        for i, num in enumerate(digits[::-1]):
            if i == 0:
                res = flag + num + 1
            else:
                res = flag + num
            digits[length-1-i] = res % 10
            flag = res // 10
        if flag:
            digits.insert(0, 1)
        return digits
