#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
ans=chk=0
for i in range(n,k+1):
    t=str(i)
    ans+=t==t[::-1]
print(ans)
