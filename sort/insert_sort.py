# -*- coding:utf-8 -*-
__author__ = 'ShawDa'

from random_list import random_int_list


def insert_sort(arr):
    length = len(arr)
    if length == 1:
        return arr
    # 从第二个数开始,从后往前找到合适的位置插入
    for i in range(1, length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


if __name__ == '__main__':
    data = random_int_list(1, 100, 10)
    print(data)
    print(insert_sort(data))
