# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x, y = len(grid), len(grid[0])
        for i in range(x):
            for j in range(y):
                if i == 0 and j != 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif i != 0 and j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif i != 0 and j != 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                else:
                    pass
        return grid[x-1][y-1]

    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x, y = len(grid), len(grid[0])
        dp, dp[0] = [0] * y, grid[0][0]
        for i in range(1, y):
            dp[i] = dp[i-1] + grid[0][i]
        for j in range(1, x):
            dp[0] = dp[0] + grid[j][0]
            for i in range(1, y):
                dp[i] = min(dp[i], dp[i-1]) + grid[j][i]
        return dp[-1]
