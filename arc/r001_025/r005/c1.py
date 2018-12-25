#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
def eof(t): print(t); exit()


h,w=map(int,input().split())
b=[set() for i in range(3)]
l=[[4 for i in range(w)] for j in range(h)]
p=[(1,0),(0,1),(-1,0),(0,-1)]
c=[]
for i in range(h):
    t=input()
    if "s" in t: b[0].add((i,t.index("s")))
    c.append(t)
while len(b[0])+len(b[1])+len(b[2]):
    for i in range(3):
        if len(b[i])>0:
            j=b[i].pop()
            for y,x in p:
                y2=j[0]+y
                x2=j[1]+x
                if 0<=y2<h and 0<=x2<w:
                    if c[y2][x2]=="g": eof("YES")
                    elif c[y2][x2]=="." and l[y2][x2]>i:
                        l[y2][x2]=i
                        b[i].add((y2,x2))
                    elif c[y2][x2]=="#" and i<2 and l[y2][x2]>i+1:
                        l[y2][x2]=i+1
                        b[i+1].add((y2,x2))

print("NO")
