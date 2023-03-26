#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: change_sort.py
Time: 2023/3/26
"""


def change_sort(arr: list):
    """
    选择排序
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    arr = [10, 2, 3, 4, 14, 2]
    print(change_sort(arr))



