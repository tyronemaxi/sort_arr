#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: merge_sort.py
Time: 2023/3/26
"""


def merge(left: list, right: list):
    """
    合并
    :param arr:
    :return:
    """
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result


def merge_sort(arr: list):
    """
    归并排序
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr

    n = len(arr)
    mid = n // 2

    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    arr = [19, 20, 1, 10, 29, 10, 1, 2, 3]
    print(merge_sort(arr))

