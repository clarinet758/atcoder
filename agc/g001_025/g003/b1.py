#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=chk=0
for i in range(n):
    a=int(input())
    ans+=(a+chk)//2
    if a>0:
         chk=(a+chk)%2
    else:
        chk=0
print(ans)
