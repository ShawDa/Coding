# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if sorted(s1+s2) != sorted(s3):
            return False
        if not s3:
            return True
        len_1, len_2, len_3 = len(s1), len(s2), len(s3)
        dp = [[False]*(len_2+1) for _ in range(len_1+1)]  # 表示s1前i个和s2前j个能否构成s3前i+j个
        for i in range(1, len_1+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, len_2+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else:
                break
        for i in range(1, len_1+1):
            for j in range(1, len_2+1):
                # 如果s1 i-1个和s2 j个为真且s1 i个和s3 i+j个相同
                if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                    continue
                # 如果s1 i个和s2 j-1个为真且s2 j个和s3 i+j个相同
                if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
        return dp[-1][-1]
