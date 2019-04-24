#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

x,k=map(int,input().split())
d=10**k
x//=d
print(x*d+d)
