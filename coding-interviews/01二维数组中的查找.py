# -*- coding:utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 左下角开始
        x, y = 0, len(array)-1
        while x < len(array[0]) and y >= 0:
            if array[y][x] == target:
                return True
            elif array[y][x] > target:
                y -= 1
            else:
                x += 1
        return False

    def Find1(self, target, array):
        # write code here
        # 右上角开始
        x, y = len(array[0]) - 1, 0
        while x >= 0 and y < len(array):
            if array[y][x] == target:
                return True
            elif array[y][x] > target:
                x -= 1
            else:
                y += 1
        return False
