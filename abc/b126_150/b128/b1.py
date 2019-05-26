#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
c,m=[],[]
d={}
t={}
for i in range(n):
    s,p=map(str,input().split())
    m.append((s,int(p)))
    if s not in c:
        c.append(s)
        d[s]=[int(p)]
    else:
        d[s].append(int(p))
    t[(s,int(p))]=i+1
c.sort()
ans={}
cnt=1
for i in c:
    d[i].sort(reverse=True)
    for j in d[i]:
        ans[cnt]=(i,j)
        cnt+=1
for i in range(1,n+1):
    print(t[ans[i]])
