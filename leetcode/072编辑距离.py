# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = len(word1), len(word2)
        if a > b:
            return self.minDistance(word2, word1)
        dp = [[0]*(b+1) for _ in range(a+1)]  # dp[i][j]表示a前i个词和b前j个词的编辑距离
        for i in range(a+1):
            dp[i][0] = i
        for j in range(b+1):
            dp[0][j] = j
        for i in range(1, a+1):
            for j in range(1, b+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[a][b]
