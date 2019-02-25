# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self.helper(n, 0, res, [0]*n)
        return res

    def helper(self, n, row, res, flag):
        """
        :param row: 行
        :param flag: index为i处的值代表i行的皇后位置
        """
        if row == n:
            res.append(self.flag2one(flag, n))
            return
        for i in range(n):  # 从上到下
            flag[row], judge = i, True  # 第row行放在第i列上
            for j in range(row):  # 判断和之前行有没有冲突
                if flag[j] == i or row-j == abs(i-flag[j]):
                    # 列冲突或者斜冲突(x和y的差一致)
                    judge = False
                    break
            if judge:  # 前一行ok
                self.helper(n, row+1, res, flag)

    def flag2one(self, flag, n):
        one = [['.']*n for i in range(n)]
        for i in range(n):
            one[i][flag[i]] = 'Q'
            one[i] = ''.join(one[i])
        return one
