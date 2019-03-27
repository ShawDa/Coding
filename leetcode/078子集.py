# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i]+[num])
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(0, nums, [])
        return self.res

    def helper(self, start, nums, tmp):
        self.res.append(tmp)
        for i in range(start, len(nums)):
            self.helper(i + 1, nums, tmp + [nums[i]])
        return
