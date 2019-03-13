# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 二分法
        left, right = 0, x
        while left <= right:
            mid = (left+right) // 2
            if mid*mid <= x:
                if (mid+1)*(mid+1) > x:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1
