#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import heapq
n,m=map(int,input().split())
q=[]
a=[-int(i) for i in input().split()]
for i in a:
    heapq.heappush(q,i)
ans=chk=0
for i in range(m):
    x=heapq.heappop(q)
    heapq.heappush(q,-(-x//2))
print(-sum(q))
