# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        cur_row, down = 0, False
        res_list = [''] * min(len(s), numRows)
        for char in s:
            res_list[cur_row] += char
            if cur_row == 0 or cur_row == numRows-1:
                down = not down
            cur_row += 1 if down else -1
        return ''.join(res_list)

    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res, cycle = '', 2*numRows-2
        for i in range(numRows):
            for j in range(0, len(s)-i, cycle):
                res += s[i+j]
                if i != 0 and i != numRows-1 and j+cycle-i < len(s):
                    res += s[j+cycle-i]  # 中间部分在斜线处的
        return res
