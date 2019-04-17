# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        x, y = len(s), len(t)
        # dp[i][j]表示s前i个中包含t前j个的子序列个数
        dp = [[0] * (y+1) for _ in range(x+1)]
        for i in range(x+1):
            dp[i][0] = 1  # t为空时结果为1
        for i in range(1, x+1):
            for j in range(1, y+1):
                if i < j:  # s部分长度一定大于t部分
                    break
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:  # 相等就要加上s前面包括t前面的个数
                    dp[i][j] += dp[i-1][j-1]
        return dp[-1][-1]
