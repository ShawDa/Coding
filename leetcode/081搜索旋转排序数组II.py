# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left, right = 0, len(nums)-1
        while left <= right:
            if (left != right and nums[left]==nums[right]):
                left += 1
                while nums[left] == nums[left-1] and left < len(nums)-1:
                    left += 1
                while nums[right] == nums[right-1] and right > 0:
                    right -= 1
            mid = (left+right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[right]:  # 左有序
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右有序
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid -1
        return False
