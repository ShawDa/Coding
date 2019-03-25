# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        rows, cols = set(), set()
        x, y = len(matrix), len(matrix[0])
        for i in range(x):
            for j in range(y):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(x):
            for j in range(y):
                if i in rows or j in cols:
                    matrix[i][j] = 0

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 既然不能用额外的标记,那么只能在mat上做标记
        if not matrix:
            return matrix
        row_flag, col_flag = False, False  # 第一行第一列是否有0
        x, y = len(matrix), len(matrix[0])
        for i in range(x):
            if matrix[i][0] == 0:
                col_flag = True
                break
        for j in range(y):
            if matrix[0][j] == 0:
                row_flag = True
                break
        for i in range(1, x):
            for j in range(1, y):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, x):
            if matrix[i][0] == 0:
                for j in range(1, y):
                    matrix[i][j] = 0
        for j in range(1, y):
            if matrix[0][j] == 0:
                for i in range(1, x):
                    matrix[i][j] = 0
        if row_flag:
            for j in range(y):
                matrix[0][j] = 0
        if col_flag:
            for i in range(x):
                matrix[i][0] = 0
