#!/bin/python3

import math
import os
import random
import re
import sys

def left_shift(n,d,arr):
    copy = [None] * n
    for i in range(n):
        copy[(i+n-d)%n]=arr[i]
    return copy

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = left_shift(n, d, a)

    print(*result)
