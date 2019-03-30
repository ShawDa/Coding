# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.helper(0, nums, [])
        return self.res

    def helper(self, start, nums, tmp):
        self.res.append(tmp.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue  # 一个for循环下不能有相同的情况,因为后续的会一样
            self.helper(i+1, nums, tmp+[nums[i]])
        return
