#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

xy=[(1,0),(-1,0),(0,1),(0,-1)]
r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
d=set([(sy-1,sx-1)])
l=[]
for i in range(r):
    l.append(list(input()))
l[sy-1][sx-1]=0
while len(d):
    y,x=d.pop()
    for i,j in xy:
        i+=y
        j+=x
        if 0<i<r-1 and 0<j<c-1:
            if l[i][j]=="." or (l[i][j] not in ["#","."] and l[y][x]+1<l[i][j]):
                l[i][j]=l[y][x]+1
                d.add((i,j))
print(l[gy-1][gx-1])
