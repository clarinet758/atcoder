#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
input=sys.stdin.readline
import heapq
xy=[(1,0),(-1,0),(0,1),(0,-1)]
wp=[(-1,-1),(-1,1),(1,1),(1,-1),(2,0),(-2,0),(0,2),(0,-2),(-2,-1),(-2,1),(2,1),(2,-1),(-1,-2),(-1,2),(1,2),(1,-2),(-2,-2),(-2,2),(2,2),(2,-2)]
    
h,w=map(int,input().split())
c1,c2=map(int,input().split())
d1,d2=map(int,input().split())
d=[list(input().rstrip()) for i in range(h)]
d[c1-1][c2-1]=0
p=[]
heapq.heappush(p,(0,c1-1,c2-1))
while len(p):
    a,b,c=heapq.heappop(p)
    for x,y in xy:
        x+=b
        y+=c
        if 0<=x<h and 0<=y<w and d[x][y]!="#":
            if d[x][y]=="." or d[x][y]>a:
                d[x][y]=a
                heapq.heappush(p,(a,x,y))
    for x,y in wp:
        x+=b
        y+=c
        if 0<=x<h and 0<=y<w and d[x][y]!="#":
            if d[x][y]=="." or d[x][y]>a+1:
                d[x][y]=a+1
                heapq.heappush(p,(a+1,x,y))

print(-1 if (d[d1-1][d2-1]=="#" or d[d1-1][d2-1]==".") else d[d1-1][d2-1])

