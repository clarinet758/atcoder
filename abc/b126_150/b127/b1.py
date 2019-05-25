#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

r,d,x=map(int,input().split())
for i in range(10):
    x=r*x-d
    print(x)
