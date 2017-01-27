#!/usr/bin/env python
# -*- coding: UTF-8 -*-

r,c=map(int,raw_input().split())
sy,sx=map(int,raw_input().split())
gy,gx=map(int,raw_input().split())
l=[]
for i in range(r):
    c=list(raw_input())
    l.append(c)
l[sy-1][sx-1]=0
q=set([(sy-1,sx-1)])
chk=[(-1,0),(1,0),(0,-1),(0,1)]
while len(q):
    w=q.pop()
    for y,x in chk:
        if l[w[0]+y][w[1]+x]=='#':
            pass
        elif l[w[0]+y][w[1]+x]=='.':
            l[w[0]+y][w[1]+x]=l[w[0]][w[1]]+1
            q.add((w[0]+y,w[1]+x))
        elif l[w[0]][w[1]]+1<l[w[0]+y][w[1]+x]:
            l[w[0]+y][w[1]+x]=l[w[0]][w[1]]+1
            q.add((w[0]+y,w[1]+x))
print l[gy-1][gx-1]

