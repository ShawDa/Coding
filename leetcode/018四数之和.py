# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, length = [], len(nums)
        nums.sort()
        for first in range(length-3):
            if sum(nums[first:first+4]) > target:
                break
            if first != 0 and nums[first] == nums[first-1]:
                continue
            threesum = target-nums[first]
            for second in range(first+1, length-2):
                if sum(nums[second:second+3]) > threesum:
                    break
                if second != first+1 and nums[second] == nums[second-1]:
                    continue
                twosum = threesum-nums[second]
                thrid, four = second + 1, length - 1
                while thrid < four:
                    sum_two = nums[thrid]+nums[four]
                    if sum_two == twosum:
                        res.append([nums[first], nums[second], nums[thrid], nums[four]])
                    if sum_two >= twosum:
                        four -= 1
                        while thrid+1 < four and nums[four] == nums[four+1]:
                            four -= 1
                    if sum_two <= twosum:
                        thrid += 1
                        while thrid+1 < four and nums[thrid] == nums[thrid-1]:
                            thrid += 1
        return res
