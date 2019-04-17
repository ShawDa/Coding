# -*- coding:utf-8 -*-
__author__ = 'ShawDa'

from random_list import random_int_list


def bubble_sort(arr):
    # 从右到左,每次确定一个最小值
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


if __name__ == '__main__':
    data = random_int_list(1, 100, 10)
    print(data)
    print(bubble_sort(data))
