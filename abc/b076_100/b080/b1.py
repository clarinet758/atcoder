#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
t=0
for i in str(n):
    t+=int(i)
print("Yes" if n%t==0 else "No")
