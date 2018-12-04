#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
l=[int(i) for i in input().split()]
ans=chk=0
for i in l:
    if i==chk:
        chk=0
        ans+=1
    else:
        chk=i
print(ans)
