#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import heapq
n,m=map(int,input().split())
a=[int(i) for i in input().split()]
d={}
l,q=[],[]
for i in a:
    if i in d: d[i]+=1
    else: d[i]=1

for i in d: heapq.heappush(q, i)

for i in range(m):
    b,c=map(int,input().split())
    l.append((c,b))
l.sort(reverse=True)

for c,b in l:
    while b:
        if len(q)==0 or c<=q[0]: break
        x=min(b,d[q[0]])
        if c in d:
            d[c]+=x
        else:
            d[c]=x
        b-=x
        d[q[0]]-=x
        if d[q[0]]==0:
            heapq.heappop(q)
ans=0        
for i in d:
    ans+=i*d[i]
print(ans)

