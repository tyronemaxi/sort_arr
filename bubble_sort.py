#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: bubble_sort.py
Time: 2023/3/26
"""
def bubble_sort(arr: list):
    """
    冒泡排序
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        exchange = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                exchange = True
        if not exchange:
            break

    return arr


if __name__ == '__main__':
    arr = [10, 1, 2, 3, 1, 4, 7]
    print(bubble_sort(arr))
