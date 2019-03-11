# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        i, j, dx, dy = 0, 0, 0, 1
        for num in range(1, n*n+1):
            res[i][j] = num
            if res[(i+dx) % n][(j+dy) % n] > 0:
                dx, dy = dy, -dx
            i += dx
            j += dy
        return res
