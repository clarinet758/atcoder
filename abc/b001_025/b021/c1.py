#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mod=10**9+7

n=int(input())
a,b=map(int,input().split())
m=int(input())
d={i:[] for i in range(1,n+1)}
for i in range(m):
    x,y=map(int,input().split())
    d[x].append(y)
    d[y].append(x)

f=set([a])
u=set([])
l=set([a]) #log
ft=[1]*(n+1)
ut=[0]*(n+1)

ans=0
while 1:
    ans+=1
    while len(f):
        x=f.pop()
        for i in d[x]:
            if i not in l:
                u.add(i)
                ut[i]=(ft[x]+ut[i])%mod
    i=len(u)
    if b in u:
        print(ut[b])
        exit()
    for j in u:
        l.add(j)
    f={u.pop() for j in range(i)}
    ft=[i%mod for i in ut]
    ut=[0]*(n+1)

