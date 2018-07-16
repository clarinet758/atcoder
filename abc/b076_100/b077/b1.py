#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pscl 要修正
n=int(input())
ans=1
while 1:
    if (ans+1)**2>n: break
    ans+=1
print(ans**2)
