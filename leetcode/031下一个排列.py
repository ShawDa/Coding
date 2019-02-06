# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 从右边往左边找到第一个i使得nums[i]<nums[i+1]
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            # 找到i+1到最后大于i的最小值的位置
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # 换位置
        # 后面的肯定是排好序的，反转就行
        nums[i+1:] = nums[i+1:][::-1]
