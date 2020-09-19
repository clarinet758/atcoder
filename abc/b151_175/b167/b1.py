#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,c,k=map(int,input().split())
ans=0
ans+=1*min(a,k)
k=max(0,k-a)
k=max(0,k-b)
ans+=-1*k
print(ans)
