# -*- coding:utf-8 -*-

import random


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


class QuickSort:
    def __init__(self,data):
        self.data = data



if __name__ == '__main__':
    data = random_int_list(1, 100, 10)
    print(data)

