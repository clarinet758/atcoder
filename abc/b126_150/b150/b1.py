#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
s=input()+"XXX"
ans=0
for i in range(n):
    if s[i]+s[i+1]+s[i+2]=="ABC": ans+=1
print(ans)
