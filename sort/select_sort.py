# -*- coding:utf-8 -*-

import random


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def select_sort(arr):
    def get_min(ar):
        index, min_num = 0, ar[0]
        for i, num in enumerate(ar[1:]):
            if num < min_num:
                index, min_num = i+1, num
        ar.pop(index)
        return min_num, ar
    length = len(arr)
    if length <= 1:
        return arr
    res = []
    while len(arr) > 1:
        min_num, arr = get_min(arr)
        res.append(min_num)
    res.append(arr[0])
    return res


if __name__ == '__main__':
    data = random_int_list(1, 100, 10)
    print(data)
    print(select_sort(data))