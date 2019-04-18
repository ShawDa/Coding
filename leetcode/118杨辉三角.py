# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = []
        for i in range(numRows):
            row = [1 for k in range(i+1)]
            row[0], row[i] = 1, 1
            if i >= 2:
                for j in range(1, i):
                    row[j] = tri[i-1][j-1] + tri[i-1][j]
            tri.append(row)
        return tri
