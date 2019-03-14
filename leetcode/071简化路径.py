# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def simplifyPath(self, path: str) -> str:
        res, stack = '', []
        list_path = path.split('/')
        for item in list_path:
            if item not in ['', '.', '..']:  # 路径
                stack.append(item)
            if item == '..' and stack:
                stack.pop(-1)
        if not stack:
            return '/'
        for one in stack:
            res += '/'+one
        return res
