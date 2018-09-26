# -*- coding:utf-8 -*-

import random


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def quick_sort0(arr):
    length = len(arr)
    if length <= 1:
        return arr
    first = arr.pop(0)
    less, more = [], []
    for num in arr:
        if num < first:
            less.append(num)
        else:
            more.append(num)
    return quick_sort0(less) + [first] + quick_sort0(more)


def quick_sort1(arr, left, right):
    def partition(ar, left, right):
        cand = ar[right]
        i = left
        for j in range(left, right):
            if ar[j] < cand:
                ar[i], ar[j] = ar[j], ar[i]
                i += 1
        ar[i], ar[right] = ar[right], ar[i]
        return i
    if left < right:
        q = partition(arr, left, right)
        quick_sort1(arr, left, q-1)
        quick_sort1(arr, q+1, right)
    return arr


def quick_sort2(arr, left, right):
    if left >= right:
        return
    stack = [left, right]
    while stack:
        low, high = stack.pop(0), stack.pop(0)
        if high - low <= 0:
            continue
        cand = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < cand:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[high], arr[i] = arr[i], arr[high]
        stack.extend([low, i-1, i+1, high])
    return arr


if __name__ == '__main__':
    data = random_int_list(1, 100, 10)
    print(data)
    # print(quick_sort0(data))
    # print(quick_sort1(data, 0, len(data)-1))
    print(quick_sort2(data, 0, len(data)-1))