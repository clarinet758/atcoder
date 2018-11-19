#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
x=[]
d=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    d[a-1].append(b-1)
    d[b-1].append(a-1)
    x.append((a-1,b-1))
ans=0
for i in x:
    t=set([i[0]])
    r=set()
    while len(t):
        o=t.pop()
        for j in d[o]:
            if j not in r and len(set([o,j])&set([i[0],i[1]]))!=2:
                r.add(j)
                t.add(j)
    if len(r)!=n: ans+=1
print(ans) 
