# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def __init__(self):
        self.s = ''

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        char_dict = {}
        for char in self.s:
            char_dict[char] = char_dict.get(char, 0) + 1
        for char in self.s:
            if char_dict[char] == 1:
                return char
        return '#'

    def Insert(self, char):
        # write code here
        self.s += char
