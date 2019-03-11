# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def get_n(n):  # 求解n的阶乘
            res = 1
            for i in range(1, n+1):
                res *= i
            return res
        ret, nums = '', list(map(str, list(range(1, n+1))))
        for i in range(n, 0, -1):
            res = get_n(i-1)
            index = (k-1) // res  # 找到第一位的位置
            ret += nums.pop(index)
            k -= res*index  # 求后面剩余数的第k个
        return ret
