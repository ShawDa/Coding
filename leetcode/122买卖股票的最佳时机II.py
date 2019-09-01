# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 找到第一个最低值和第一个最高值，加上差值，依次向后找，总而言之就是找增加的那几段
        max_profit = 0
        for i in range(len(prices)-1):
            differ = prices[i+1] - prices[i]
            if differ > 0:
                max_profit += differ
        return max_profit
