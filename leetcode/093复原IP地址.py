# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        if len(s) > 12:
            return self.res
        self.helper(s, [])
        return self.res

    def helper(self, s, tmp):
        if not s and len(tmp) == 4:
            self.res.append('.'.join(tmp.copy()))
            return
        for i in range(1, 4):  # 取一位到三位
            if i > len(s):
                break
            num = int(s[:i])
            if str(num) == s[:i] and num <= 255:  # 不以0开头
                self.helper(s[i:], tmp+[s[:i]])
