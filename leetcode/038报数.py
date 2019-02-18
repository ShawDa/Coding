# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ['1']
        for i in range(1, n):
            before, here, count = res[i-1], '', 1
            for j, num in enumerate(before):
                if j == 0:
                    cand = num
                    continue
                if cand == num:
                    count += 1
                else:
                    here += str(count) + str(cand)
                    cand, count = num, 1
            here += str(count) + str(cand)
            res.append(here)
        return res[-1]
