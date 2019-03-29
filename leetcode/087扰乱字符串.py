# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # s1分为s11和s12,s2分为s21和s22,如果s11和s21成立且s12和s22成立
        # 或者s11和s22成立且s12和s21成立,s1和s2就成立
        if sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
