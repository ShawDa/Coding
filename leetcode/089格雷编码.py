# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def grayCode(self, n: int) -> List[int]:
        # G(i) = i ^ (i/2)
        res = []
        for i in range(2**n):
            res.append(i ^ (i//2))
        return res
