#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
    tmp,cnt=0,i
    while i:
        tmp+=i%10
        i//=10
    if a<=tmp<=b: ans+=cnt
print(ans)

