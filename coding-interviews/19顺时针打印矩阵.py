# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        if not matrix or not matrix[0]:
            return res
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left <= right and top <= bottom:
            for j in range(left, right+1):
                res.append(matrix[top][j])
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            if top < bottom:
                for j in range(right-1, left, -1):
                    res.append(matrix[bottom][j])
            if left < right:
                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res

    def printMatrix1(self, matrix):
        # write code here
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            if not matrix or not matrix[0]:
                break
            matrix = self.rotate(matrix)
        return res

    def rotate(self, mat):
        new = []
        for j in range(len(mat[0])-1, -1, -1):
            new.append([row[j] for row in mat])
        return new
