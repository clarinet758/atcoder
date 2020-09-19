#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys

n=int(input())
b=[int(i) for i in input().split()]
d=[int(i)+1 for i in range(n)]
t=n-1
ans=[]
while 1:
    f=1
    for i in range(t,-1,-1):
        if b[i]==d[i]:
            f=0
            ans.append(i+1)
            for j in range(i,n-1):
                b[j]=b[j+1]
            b[n-1]=0
            break
    if len(ans)==n:
        break
    if f:
        print(-1)
        exit()
for i in ans[::-1]:
    print(i)

