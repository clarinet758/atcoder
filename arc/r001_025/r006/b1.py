#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,l=map(int,input().split())
w=[input() for i in range(l)]
t=input()
ans=t.index("o")
for i in range(l-1,-1,-1):
    if ans-2>-1 and w[i][ans-1]=="-":
        ans-=2
    elif ans+2<n*2-1 and w[i][ans+1]=="-":
        ans+=2
print(ans//2+1)
