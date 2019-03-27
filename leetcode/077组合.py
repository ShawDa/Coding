# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res, self.tmp = [], []
        self.helper(n, k, 1)
        return self.res

    def helper(self, n, k, start):
        if len(self.tmp) == k:
            self.res.append(self.tmp.copy())
            return
        for i in range(start, n+1):
            self.tmp.append(i)
            self.helper(n, k, i+1)
            self.tmp.pop()

    def combine1(self, n: int, k: int):
        self.res, self.tmp = [], []
        self.helper1(n, k, 1)
        return self.res

    def helper1(self, n, k, start):
        if len(self.tmp) == k:
            self.res.append(self.tmp.copy())
            return
        for i in range(start, n-(k-len(self.tmp))+2):
            self.tmp.append(i)
            self.helper(n, k, i+1)
            self.tmp.pop()
