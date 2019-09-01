# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 前n天的最大利润 = max(前n-1天最大利润， 第n天price - 前n-1天最小price)
        max_profit = 0
        for i, price in enumerate(prices):
            if i == 0:
                min_price = price
                continue
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
