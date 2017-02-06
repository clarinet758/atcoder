#!/usr/bin/env python
# -*- coding: UTF-8 -*-

xy=[(1,0),(-1,0),(0,1),(0,-1)]

h,w=map(int,raw_input().split())
c=[]
s0=set()
s1=set()
s2=set()

def yes():
    print 'YES'
    exit()

for i in range(h):
    tmp=list(raw_input())
    if 's' in tmp:
        s0.add((i,tmp.index('s')))
        tmp[tmp.index('s')]=0
    c.append(tmp)

while len(s0):
    t=s0.pop()
    for y,x in xy:
        ty=t[0]+y
        tx=t[1]+x
        if 0<=ty<h and 0<=tx<w:
            if c[ty][tx]=='.':
                c[ty][tx]=0
                s0.add((ty,tx))
            elif c[ty][tx]=='#':
                c[ty][tx]=1
                s1.add((ty,tx))
            elif c[ty][tx]=='g':
                yes()

while len(s1): 
    t=s1.pop()
    for y,x in xy:
        ty=t[0]+y
        tx=t[1]+x
        if 0<=ty<h and 0<=tx<w:
            if c[ty][tx]=='.':
                c[ty][tx]=1
                s1.add((ty,tx))
            elif c[ty][tx]=='#':
                c[ty][tx]=2
                s2.add((ty,tx))
            elif c[ty][tx]=='g':
                yes()
while len(s2):
    t=s2.pop()
    for y,x in xy:
        ty=t[0]+y
        tx=t[1]+x
        if 0<=ty<h and 0<=tx<w:
            if c[ty][tx]=='.':
                c[ty][tx]=2
                s2.add((ty,tx))
            elif c[ty][tx]=='g':
                yes()
print 'NO'
