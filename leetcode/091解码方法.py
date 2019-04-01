# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s)+1)
        for i in range(len(s)):
            dp[i+1] = 0 if s[i] == '0' else dp[i]
            if i > 0 and 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]  # 如果能走两步到这
        return dp[-1]
