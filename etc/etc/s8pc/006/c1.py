#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

h,w=map(int,input().split())
d=[]
if h==1:
    print("Yay!" if "#" not in input() else ":(")
else:
    f=1
    for i in range(h):
        a=input()
        if f and "#" not in a: f=0
        d.append(a)
    if f:
        print(":(")
    else:
        s=set([(0,0)])
        while len(s):
            y,x=s.pop()
            if y+1<h and d[y+1][x]!="#":
                s.add((y+1,x))
            if x+1<w and d[y][x+1]!="#":
                s.add((y,x+1))
            if (y+1==h-1 and x==w-1) or (y==h-1 and x+1==w-1):
                print("Yay!")
                exit()
        print(":(")

