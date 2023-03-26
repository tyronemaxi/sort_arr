#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: quick_sort.py
Time: 2023/3/26
"""
import random


def quick_sort(arr: list):
    """
    快排
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr

    privot = arr[0]
    less = [i for i in arr[1:] if i <= privot]
    greater = [i for i in arr[1:] if i > privot]

    return quick_sort(less) + [privot] + quick_sort(greater)


if __name__ == '__main__':
    arr = [19, 20, 1, 10, 29, 10, 1, 2, 3]
    print(quick_sort(arr))