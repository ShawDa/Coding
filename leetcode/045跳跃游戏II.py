# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, step = 0, 0  # res:步数,step:指针位置
        while step < len(nums)-1:
            if step+nums[step] >= len(nums)-1:
                return res+1
            tmp = step
            for i in range(step+1, step+nums[step]+1):
                if i+nums[i] > tmp+nums[tmp]:
                    tmp = i  # i<len(nums)-1
            step = tmp
            res += 1
        return res  # [0]
