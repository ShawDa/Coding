# -*- coding:utf-8 -*-
__author__ = 'ShawDa'

from random_list import random_int_list


def select_sort(arr):
    for i in range(len(arr)):
        tmp = min(arr[i:])
        tmp_index = arr[i:].index(tmp)
        arr[i], arr[i + tmp_index] = arr[i + tmp_index], arr[i]
    return arr


if __name__ == '__main__':
    data = random_int_list(1, 100, 10)
    print(data)
    print(select_sort(data))
