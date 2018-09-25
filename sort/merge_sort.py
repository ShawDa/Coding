# -*- coding:utf-8 -*-

import random


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    mid = int(length/2)
    left, right = arr[0:mid], arr[mid:]
    left, right = merge_sort(left), merge_sort(right)
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