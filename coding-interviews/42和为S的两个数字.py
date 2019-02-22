# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        left, right, res = 0, len(array)-1, []
        while left < right:
            here_sum = array[left] + array[right]
            if here_sum > tsum:
                right -= 1
            elif here_sum < tsum:
                left += 1
            else:
                res.extend([array[left], array[right]])
                break
        return res
