#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
l,r=[],[]
for i in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
l.sort()
l.sort(key=lambda a: a[1],reverse=True)
for i in range(n):
    x,y=map(int,input().split())
    r.append((x,y))
r.sort()
ans=0
chk=[1]*n
for i in range(n):
    for j in range(n):
        if l[i][0]<r[j][0] and l[i][1]<r[j][1] and chk[j]:
            chk[j]=0
            ans+=1
            break
print(ans)
