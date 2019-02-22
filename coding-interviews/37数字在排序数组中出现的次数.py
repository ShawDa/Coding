# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # 因为都是整数,所以可以看成是找k-0.5和k+0.5的插入位置
        return self.bi_search(data, k+0.5) - self.bi_search(data, k-0.5)

    def bi_search(self, data, num):
        left, right = 0, len(data)-1
        while left <= right:
            mid = (left+right) // 2
            if data[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        return left
