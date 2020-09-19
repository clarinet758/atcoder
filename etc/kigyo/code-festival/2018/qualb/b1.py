#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,x=map(int,input().split())
ans=chk=0
for i in range(n):
    a,b=map(int,input().split())
    chk=max(chk,b)
    ans+=a*b
print(ans+chk*x)
