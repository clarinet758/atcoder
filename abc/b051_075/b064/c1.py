#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
l=[int(i) for i in input().split()]
cnt=[0]*9
ans=0
for i in l:
    if i>3199:
        i=3200
    cnt[i//400]+=1
for p in range(8):
    i=cnt[p]
    if i!=0:
        ans+=1
print(ans if ans!=0 else 1,ans+cnt[-1])
