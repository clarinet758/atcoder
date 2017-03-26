#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
g={int(i):[] for i in range(n)}
for i in range(n):
    x,y=map(int,input().split())
    g[i].append((x,y))

for i in range(m):
    x,y=map(int,input().split())
    for j in range(n):
        tmp=abs(g[j][0][0]-x)+abs(g[j][0][1]-y)
        if i==0:
            g[j].append(tmp)
            g[j].append(i)
        elif tmp<g[j][1]:
            g[j][1]=tmp
            g[j][2]=i
for i in range(n):
    print(g[i][2]+1)


