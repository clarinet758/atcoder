#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
f=[]
for i in range(n):
    f.append([int(i) for i in input().split()])
p=[]
for i in range(n):
    p.append([int(i) for i in input().split()])

cnt=[0]*n
ans=tmp=0
for i in range(1,1<<10):
    tmp=0
    cnt=[0]*n
    for j in range(10):
        if (i&(1<<j)):
            for k in range(n):
                if (f[k][j]): cnt[k]+=1
    for l in range(n):
       tmp+=p[l][cnt[l]]
    if i==1: ans=tmp
    else: ans=max(ans,tmp)

print(ans)
