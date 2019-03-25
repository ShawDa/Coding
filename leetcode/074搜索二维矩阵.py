# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        x, y = len(matrix), len(matrix[0])
        i, j = x-1, 0
        while i >= 0 and j <= y-1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
