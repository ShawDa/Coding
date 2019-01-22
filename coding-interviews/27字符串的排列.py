# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def Permutation(self, ss):
        # write code here
        res = set()
        if ss == '':
            return res
        if len(ss) == 1:
            return [ss]
        for i, char in enumerate(ss):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                res.add(char+j)
        return sorted(list(res))
