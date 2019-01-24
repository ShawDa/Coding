# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        def sort(x, y):
            if x + y > y + x:
                return 1
            elif x + y == y + x:
                return 0
            else:
                return -1
        from functools import cmp_to_key
        numbers = list(map(str, numbers))
        numbers.sort(key=cmp_to_key(lambda x, y: sort(x, y)))
        return ''.join(numbers)
