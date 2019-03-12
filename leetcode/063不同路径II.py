# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                for k in range(j, n):
                    dp[0][k] = 0
                break
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                for k in range(i, m):
                    dp[k][0] = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
        return dp[m-1][n-1]
