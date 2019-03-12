# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 总共走m+n-2步，其中m-1步向下走
        res = 1
        for num in range(n, m+n-1):
            res *= num
        for num in range(1, m):
            res //= num
        return res
