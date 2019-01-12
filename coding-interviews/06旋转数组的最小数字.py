# -*- coding:utf-8 -*-


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        left, right = 0, len(rotateArray)-1
        while left < right:
            mid = (left+right) // 2
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[left]:
                right = mid
            else:
                right -= 1
        return rotateArray[left]
