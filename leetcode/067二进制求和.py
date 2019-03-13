# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a, len_b = len(a), len(b)
        if len_b > len_a:
            return self.addBinary(b, a)
        list_a, list_b, flag = list(a)[::-1], list(b)[::-1], 0
        for i in range(len_a):
            if i >= len_b:
                break
            res = flag + int(list_a[i]) + int(list_b[i])
            if res == 3:
                flag = 1
                list_a[i] = '1'
            elif res == 2:
                flag = 1
                list_a[i] = '0'
            else:
                flag = 0
                list_a[i] = str(res)
        if flag == 0:
            return ''.join(list_a[::-1])
        for i in range(len_b, len_a):
            res = flag + int(list_a[i])
            if res == 2:
                flag = 1
                list_a[i] = '0'
            else:
                flag = 0
                list_a[i] = str(res)
        if flag == 1:
            list_a.append('1')
        return ''.join(list_a[::-1])
