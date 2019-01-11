# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, area = 0, len(height)-1, 0
        while left < right:
            area = max(area, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, area = 0, len(height)-1, 0
        while left < right:
            min_height = min(height[left], height[right])
            area = max(area, min_height*(right-left))
            while height[left] <= min_height and left < right:
                left += 1
            while height[right] <= min_height and left < right:
                right -= 1
        return area
