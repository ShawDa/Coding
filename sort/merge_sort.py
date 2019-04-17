# -*- coding:utf-8 -*-
__author__ = 'ShawDa'

from random_list import random_int_list


def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    mid = int(length / 2)
    left, right = arr[:mid], arr[mid:]
    left, right = merge_sort(left), merge_sort(right)
    # 两个有序list合并
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res += left
    if right:
        res += right
    return res


if __name__ == '__main__':
    data = random_int_list(1, 100, 10)
    print(data)
    print(merge_sort(data))
