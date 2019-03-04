# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        # 数组长度为5,除0外其它数个数不超过1，除0外其它数相差小于等于4
        if len(numbers) != 5:
            return False
        num_dict, min_num, max_num = {}, 14, -1
        for num in numbers:
            if num == 0:
                continue
            if num in num_dict:
                return False
            else:
                num_dict[num] = 1
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        if max_num - min_num <= 4:
            return True
        else:
            return False
