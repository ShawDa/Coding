# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict[char] + 1 if char in s_dict else 1
        for i, char in enumerate(s):
            if s_dict[char] == 1:
                return i
        return -1

    def FirstNotRepeatingChar1(self, s):
        # write code here
        for i, char in enumerate(s):
            if s.count(char) == 1:
                return i
        return -1
