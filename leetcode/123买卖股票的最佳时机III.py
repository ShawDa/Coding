# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        设置四个变量，分别表示：
        在该天第一次买入的最大收益，为max(第一次买的最大收益,这一次的价格负值);
        在该天第一次卖出的最大收益，为max(第一次卖的最大收益,这一次价格加上第一次买的最大收益)；
        在该天第二次买入的最大收益，为max(第二次买的最大收益,第一次卖的最大收益减去这一次的价格)；
        在该天第二次卖出的最大收益，为max(第二次卖的最大收益,这一次价格加上第二次买的最大收益).
        注意：买入时要算收益的话为负值
        """
        import sys
        first_buy, first_sell, second_buy, second_sell = -sys.maxsize, 0, -sys.maxsize, 0
        for price in prices:
            first_buy = max(first_buy, -price)  # 第一次买入手上的钱
            first_sell = max(first_sell, price+first_buy)  # 第一次卖出手上的钱
            second_buy = max(second_buy, first_sell-price)  # 第二次买入手上的钱
            second_sell = max(second_sell, price+second_buy)  # 第二次卖出手上的钱
        return second_sell

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 动态规划，其中left表示从0到i这部分一次买卖赚取的利润，right表示从j到length-1这部分一次买卖赚取的利润，它们相加取最大值就是最终的结果
        if len(prices) <= 1:
            return 0
        left, right = [0]*len(prices), [0]*len(prices)
        min_price, max_price = prices[0], prices[-1]
        for i in range(1, len(prices)):
            left[i] = max(left[i-1], prices[i]-min_price)
            min_price = min(min_price, prices[i])
        for j in range(len(prices)-2, -1, -1):
            right[j] = max(right[j+1], max_price-prices[j])
            max_price = max(max_price, prices[j])
        res = [left[k]+right[k] for k in range(len(prices))]
        return max(res)
