# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        for i in range(rowIndex+1):
            row = [1] * (i+1)
            if i >= 2:
                for j in range(1,i):
                    row[j] = tmp[j-1] + tmp[j]
            tmp = row
        return tmp

    def getRow1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex+1)
        if rowIndex >= 1:
            for i in range(1, rowIndex+1):
                row[i] = row[i-1]*(rowIndex+1-i)//i
        return row
