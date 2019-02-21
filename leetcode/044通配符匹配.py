# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        # dp[i][j]表示s的前i个字符和p的前j个字符是否匹配
        dp = [[False] * (len_p+1) for _ in range(len_s+1)]
        dp[0][0] = True
        for i in range(1, len_p+1):
            if p[i-1] == '*':  # p首部有‘*’那么就可以匹配
                dp[0][i] = dp[0][i-1]
        for i in range(1, len_s+1):  # 从左到右从上到下
            for j in range(1, len_p+1):
                if p[j-1] == '*':  # 如果p位置处为*,那么可匹配所有
                    dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1])
        return dp[len_s][len_p]
