#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
x,t=n,0
while x:
    t+=x%10
    x//=10
print("Yes" if n%t==0 else "No")
