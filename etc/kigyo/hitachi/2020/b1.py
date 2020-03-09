#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,m=map(int,input().split())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]

ans=99999999999
ans=min(A)+min(B)
for i in range(m):
    x,y,c=map(int,input().split())
    ans=min(ans,A[x-1]+B[y-1]-c)
print(ans)
