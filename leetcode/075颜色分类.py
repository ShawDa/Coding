# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict_nums = {0:0, 1:0, 2:0}
        for num in nums:
            dict_nums[num] += 1
        a, b, c = dict_nums[0], dict_nums[1], dict_nums[2]
        nums[:a] = [0] * a
        nums[a:a+b] = [1] * b
        nums[a+b:a+b+c] = [2] * c

    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 两个指针代表0,2的位置，排好0和2就行
        left, right, i = 0, len(nums)-1, 0
        while i <= right:
            if nums[i] == 0:  # 0放左边
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:  # 2放右边
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
