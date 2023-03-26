#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: insert_sort.py
Time: 2023/3/26
"""


def insert_sort(arr: list):
    """
    插入排序
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j+1] = value

    return arr


if __name__ == '__main__':
    arr = [10, 2, 3, 4, 14, 2]
    print(insert_sort(arr))