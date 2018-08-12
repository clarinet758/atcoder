#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())

for i in range(25):
    for j in range(25):
        if n==i*4+j*7:
            print("Yes")
            exit()

print("No")
