#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,w=map(int,input().split())
d={}
p=0
for i in range(n):
    a,b=map(int,input().split())
    if a in d: d[a].append(b)
    else: d[a]=[b]
    p=max(p,a)

for i in range(4):
    if p-i in d:d[p-i].sort(reverse=True)
    else: d[p-i]=[0]

l={}
for i in d:
    t=0
    l[i]=[0]
    for j in d[i]:
        t+=j
        l[i].append(t)
ans=0
for ai,i in enumerate(l[p]):
    for bj,j in enumerate(l[p-1]):
        for ck,k in enumerate(l[p-2]):
            for em,m in enumerate(l[p-3]):
                x=ai*p+bj*(p-1)+ck*(p-2)+em*(p-3)
                if x<=w:
                    ans=max(ans,i+j+k+m)
print(ans)
