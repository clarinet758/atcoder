#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
if k==0:
    print(n*n)
    exit()
ans=0
for i in range(k+1,n+1):
    ans+=((n+1)//i)*(i-k)+max(0,((n+1)%i-k))
print(ans)
