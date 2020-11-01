#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=chk=0
for i in range(n):
    a,b=map(int,input().split())
    ans+=(b*(b+1)//2)-(a*(a-1)//2)
print(ans)
