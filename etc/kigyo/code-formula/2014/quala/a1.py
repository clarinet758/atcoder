#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a=int(input())
ans=0
for i in range(1,10**5+1,1):
    if i**3==a:
        ans=1
        break
print(["NO","YES"][ans])
