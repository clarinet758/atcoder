#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n,x=map(int,input().split())
s=input()
ans=0
for i in range(n):
    t=int(input())
    if s[i]=="1": ans+=min(t,x)
    else: ans+=t
print(ans)
