#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline

n=int(input())
if n==100000:
    print(90909)
elif n<100:
    print(min(9,n))
elif n<1000:
    print(9+(n-99))
elif n<10000:
    print(909)
else:
    print(909+(n-9999))
