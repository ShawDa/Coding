# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res, max_sum = array[0], array[0]
        for num in array[1:]:
            res = max(num, res+num)
            max_sum = max(max_sum, res)
        return max_sum
