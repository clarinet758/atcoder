#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from collections import deque
mod=10**9+7
ans=chk=0
w=[0]*200
a,b=map(int,input().split())
w[a]=1
d=deque([mod,a])
p=[-10,-5,-1,1,5,10]
while 1:
    x=d.pop()
    if x==b:
        print(ans)
        exit() 
    if x==mod:
        ans+=1
        d.appendleft(mod)
        continue
    for i in p:
        if w[x+i]==0:
            w[x+i]=1
            d.appendleft(x+i)
