#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n=int(input())
l=[abs(int(i)) for i in input().split()]
print(sum(l))
y=0
for i in l:
    y+=i**2
print(y**0.5)
print(max(l))

