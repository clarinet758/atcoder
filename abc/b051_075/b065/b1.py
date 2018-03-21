#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=0
p=1
chk=[0]*n
l=[]
for i in range(n):
    l.append(int(input()))

while 1:
    if chk[p-1]==1:
        print(-1)
        break
    chk[p-1]=1
    ans+=1
    if l[p-1]==2:
        print(ans)
        break
    p=l[p-1]
    
