# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for i in range(len(triangle)-2, -1, -1):  # 自底向上
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                res[j] = triangle[i][j] + min(res[j], res[j+1])
        return res[0]
