#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d=[]
for i in range(n):
    a,b=map(int,input().split())
    d.append((a,b))
d.sort()
ans=chk=0
for i in d:
    if i[0]>chk:
        chk=i[1]
        ans+=1
    else:
        chk=max(chk,i[1])
print(ans)
