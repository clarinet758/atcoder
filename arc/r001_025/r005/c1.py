#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
def eof(t): print(t); exit()


h,w=map(int,input().split())
b=set()
l=[[4 for i in range(w)] for j in range(h)]
p=[(1,0),(0,1),(-1,0),(0,-1)]
c=[]
for i in range(h):
    t=input()
    if "s" in t: b.add((i,t.index("s")))
    c.append(t)
for i in range(3):
    d=set()
    while len(b):
        j=b.pop()
        for y,x in p:
            y2=j[0]+y
            x2=j[1]+x
            if 0<=y2<h and 0<=x2<w:
                if c[y2][x2]=="g": eof("YES")
                elif c[y2][x2]=="." and l[y2][x2]>i:
                    l[y2][x2]=i
                    b.add((y2,x2))
                elif c[y2][x2]=="#" and i<2 and l[y2][x2]>i+1:
                    l[y2][x2]=i+1
                    d.add((y2,x2))
    b=set([i for i in d])

print("NO")
