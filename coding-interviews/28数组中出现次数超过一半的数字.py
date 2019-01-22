# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        candi, count, candi_count = numbers[0], 1, 0
        for num in numbers[1:]:
            if count == 0:
                candi, count = num, 1
            elif candi == num:
                count += 1
            else:
                count -= 1
        for num in numbers:
            if num == candi:
                candi_count += 1
        return candi if 2*candi_count > len(numbers) else 0
