# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 把每一层看成一个直方图求最大矩形面积
        if not matrix:
            return 0
        array, res = [0] * len(matrix[0]), 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    array[j] = 0
                else:
                    array[j] += 1
            res = max(res, self.max_rect(array))
        return res

    def max_rect(self, array):
        array.append(0)
        stack, res = [-1], 0 # 注意这里的-1很精髓
        for i, num in enumerate(array):
            while len(stack) > 1 and num < array[stack[-1]]:
                height = array[stack.pop(-1)]
                res = max(res, height*(i-1-stack[-1]))
            stack.append(i)
        array.pop(-1)
        return res
