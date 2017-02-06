#!/usr/bin/env python
# -*- coding: UTF-8 -*-

xy=[(1,0),(-1,0),(0,1),(0,-1)]

h,w=map(int,raw_input().split())
c=[]
s=[set() for i in range(4)]


for i in range(h):
    tmp=list(raw_input())
    if 's' in tmp:
        s[0].add((i,tmp.index('s')))
    c.append(tmp)

def sol(v):
    while len(s[v]):
        t=s[v].pop()
        for y,x in xy:
            ty,tx=t[0]+y,t[1]+x
            if 0<=ty<h and 0<=tx<w:
                if c[ty][tx]=='.' or c[ty][tx]=='#':
                    s[v+[0,1][c[ty][tx]=='#']].add((ty,tx))
                    c[ty][tx]=v+[0,1][c[ty][tx]=='#']
                elif c[ty][tx]=='g':
                    print 'YES'
                    exit()

for i in range(3):
    sol(i)

print 'NO'

