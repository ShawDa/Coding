# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length <= 2:
            return 0
        left, right = [0] * length, [0] * length  # 左边最高的和右边最高的
        for i in range(1, length):
            left[i] = max(left[i-1], height[i-1])
        for j in range(length-2, -1, -1):
            right[j] = max(right[j+1], height[j+1])
        res = 0
        for k in range(1, length-1):  # 找左右较低的然后减去高度
            res += max(0, min(left[k], right[k]) - height[k])
        return res
