#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

ans=chk=0
h,w=map(int,input().split())
d=[[0]*w for i in range(h)]
l=[]
for i in range(h):
    a=input()
    chk+=a.count("#")
    l.append(a)
p=set([(0,0)])
while len(p):
    a,b=p.pop()
    for y,x in xy:
        y+=a
        x+=b
        if 0<=y<h and 0<=x<w and l[y][x]!="#":
            if d[y][x]==0 or d[y][x]>d[a][b]+1:
                d[y][x]=d[a][b]+1
                p.add((y,x))

print(-1 if d[h-1][w-1]==0 else h*w-1-chk-d[h-1][w-1])
