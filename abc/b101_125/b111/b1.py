#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
for i in range(n,1000):
    if i%111==0:
        print(i)
        exit()
