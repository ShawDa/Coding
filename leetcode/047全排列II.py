# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for one in self.permuteUnique(nums[0:i] + nums[i + 1:]):
                if [nums[i]] + one not in res:
                    res.append([nums[i]] + one)
        return res

    def permuteUnique1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res, note = [], []
        for i, num in enumerate(nums):
            if num in note:
                continue
            else:
                note.append(num)
            for one in self.permuteUnique(nums[:i]+nums[i+1:]):
                res.append([num]+one)
        return res
