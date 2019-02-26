# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = self.helper(matrix)
        return res

    def helper(self, mat):
        new = []
        if not mat:
            return new
        for i in range(len(mat[0])-1, -1, -1):
            new.append([mat[j][i] for j in range(len(mat))])
        return new

    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res, x, y, i, j, dx, dy = [], len(matrix), len(matrix[0]), 0, 0, 0, 1
        for _ in range(x*y):
            res.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i+dx)%x][(j+dy)%y] == None:  # 如果下一个位置已经走过那么就要改变方向
                dx, dy = dy, -dx
            i += dx
            j += dy
        return res
