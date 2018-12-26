#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
def eof(t): print(t); exit()
ans=1
n,m=map(int,input().split())
l=[[] for i in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    l[x-1].append(y-1)
    l[y-1].append(x-1)
for i in range(1<<n):
    chk=0
    f=1
    for j in range(n):
        if (i>>j&1)==0: continue
        chk+=1
        for k in range(j+1,n):
            if (i>>k&1)==0: continue
            if k not in l[j]: f=0
    if (f): ans=max(ans,chk)
print(ans)
