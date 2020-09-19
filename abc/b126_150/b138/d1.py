#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline

def dfs(v,p=-1):
    for u in d[v]:
        if (u==p): continue
        w[u]+=w[v];
        dfs(u,v)

d={}
n,q=map(int,input().split())
for i in range(n-1):
    a,b=map(int,input().split())
    if a in d:
        d[a].add(b)
    else:
        d[a]=set([b])
    if b in d:
        d[b].add(a)
    else:
        d[b]=set([a])
w=[0]*(n+1)

for i in range(q):
    p,x=map(int,input().split())
    w[p]+=x
dfs(1)

print(*w[1:])

#if __name__=="__main__":
#    sol()
