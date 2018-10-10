#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

xy=[(1,0),(-1,0),(0,1),(0,-1)]

h,w=map(int,input().split())
l=[]
for i in range(h):
    l.append(input())
for i in range(h):
    for j in range(w):
        if l[i][j]=="#":
            f=0
            for x,y in xy:
                if 0<=(i+y)<h and 0<=(j+x)<w and l[i+y][j+x]=="#": f=1
            if f==0:
                print("No")
                exit()
                

print("Yes")
