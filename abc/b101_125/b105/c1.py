#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=""
while n!=0:
    if n%2!=0:
        n-=1
        ans="1"+ans
    else:
        ans="0"+ans
    n=-n>>1
print(ans if ans!="" else 0)
