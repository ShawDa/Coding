# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, tmp = nums[0], nums[0]
        for num in nums[1:]:
            tmp = max(tmp+num, num)
            res = max(res, tmp)
        return res
