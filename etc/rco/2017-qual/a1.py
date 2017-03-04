#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
xy=[(1,0),(-1,0),(0,1),(0,-1)]

h,w,k=map(int,input().split())
l=[]
for i in range(h):
    l.append(input())
ans=[]
for i in range(h):
    for j in range(w):
        if l[i][j]!='0':
            ans.append((i+1,j+1))
            for k in range(7):
                ny=ans[-1][0]-1
                nx=ans[-1][1]-1
                for y,x in xy:
                    if 0<=ny+y<h and 0<=nx+x<w and l[ny+y][nx+x]!='0':
                        ans.append((ny+y+1,nx+x+1))
                        break
        if len(ans)==8:
            break
    if len(ans)==8:
        break
print(1)
for i in range(8):
    print(ans[i][0],ans[i][1])
