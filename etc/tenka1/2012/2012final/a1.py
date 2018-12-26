#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
print(sum([i**2 for i in range(1,n+1)])%m)
